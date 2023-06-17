import numpy as np
from csdl.rep.operation_node import OperationNode
import pickle
from copy import copy
import networkx as nx
from python_csdl_backend import Simulator
import gc
import matplotlib.pyplot as plt
import pandas as pd
from hashlib import sha256
import pickle
import os
from importlib import import_module
from pkg_resources import resource_filename
from time_prediction_v5.data_collection.tf_builder import tf

print ("call top")
regressions = {}
source_nodes = tf.get_source_nodes ()

def predict_time(rep, manual_wait_time = 0.005):
    """
    Predicts the time of a CSDL Model by iterating through each VariableNode, and either calling predict_operation_time or predict_manual_time.
    predict_operation_time is called for operations in the standard library that have a saved surrogate model, while predict_manual_time is 
    called for explicit/implicit operations and any other operations that don't have a saved surrogate model. Multiplies by the calibration constant
    value saved in the package to adjust for timing differences between computers. If inaccurate predictions are being produced, try recalibrating 
    the package.

    Parameters:
    -----------
    rep: GraphRepresentation
        The GraphRepresentation of the CSDL Model

    Returns:
    --------
    total_time: float
        The predicted amount of time that the Model will take to execute
    """
    graph = rep.flat_graph
    total_time = 0
    if (os.path.isfile ('./timing/cache.csv')):
        df = pd.read_csv ("./timing/cache.csv")
    else:
        if not os.path.isdir ('./timing'):
            os.mkdir ('./timing')
        pre_saved=False
        template = {'hash':[],
                    'time':[]}
        df = pd.DataFrame (template)
        df.to_csv ('./timing/cache.csv', index=False, columns=['hash', 'time'])
    for node in graph:
       if isinstance (node, OperationNode):
            op_name = str(node.op).split ()[0].split('.')[-1]
            if (op_name in source_nodes):
                time = predict_operation_time (graph, node)
            else:
                time, df = predict_manual_time (rep, node, df, manual_wait_time)
            node.execution_time = time
            if not time <=0:
                total_time += time
    print (df)
    df.to_csv('./timing/cache.csv', mode='a', index=False, header=False)
    filepath = resource_filename('time_prediction_v5', 'calibration/calibration_const.txt')
    with open(filepath) as f:
        calibration_const = int (f.readline())
    return total_time*calibration_const

def predict_manual_time (rep, node, df, manual_wait_time):

    """
    Predicts the execution time of a given node in a computation graph by either retrieving it from a cache file or computing it manually.

    Args:
    rep (GraphRepresentation): A GraphRepresentation of a CSDL Model
    node (object): A node in the computation graph.

    Returns:
    t - float: The predicted execution time of the node.
    """
    pre_saved = False
    # node_hash = hash (node)
    # node_hash = sha256 (pickle.dumps (node)).hexdigest ()
    # node_hash = repr (node)
    node_hash = str(node.name)
    # print (node.op)
    pre_saved = node_hash in list (df['hash'])
    if (pre_saved):
        t = df ['time'][list (df['hash']).index (node_hash)]
        print (t)
        print ("used cache")
    else:
        # print ("predicting manual time for: ", str(node.op).split ()[0].split('.')[-1])
        rep2 = copy(rep)
        rep2.flat_graph = nx.DiGraph()
        rep2.flat_graph.add_node(node)
        rep2.flat_graph.add_edges_from (rep.flat_graph.in_edges (node))
        rep2.flat_graph.add_edges_from (rep.flat_graph.out_edges (node))

        sim = Simulator(rep2)
        sim.run ()
        num_iters = 0
        total_time = 0
        while total_time <=manual_wait_time: #make this adaptive, num_iters <= 5 or 
            # print (num_iters, total_time)
            total_time+=sim.run ()
            num_iters+=1
        t = total_time/num_iters
        if (t<=1e-6):
            t = 1e-6
        data = {'hash':[node_hash],
                'time':[t]}
        df2 = pd.DataFrame(data)
        # pd.concat (df, df2)
        # df.append (data, ignore_index = True)
        df = pd.concat ([df, df2], ignore_index=True)
        del (rep2)
        del (sim)
        gc.collect()
    return t, df

def predict_operation_time (graph, node):
    """
    Predicts the execution time of a given node in a computation graph by using the saved surrogate model for that respective operation

    Args:
    graph (object): A computation graph representation of the CSDL Model
    node (object): A node in the computation graph.

    Returns:
    time - float: The predicted execution time of the node.
    """
    # print (source_nodes)
    op_name = str(node.op).split ()[0].split('.')[-1]
    if (len (source_nodes[op_name]) > 1):
        for variant in source_nodes[op_name]:
            if (tf.operations [variant].checker (graph, node)):
                op_name = variant
    param_vals = {}

    if op_name not in regressions:
        
        filename = resource_filename ('time_prediction_v5', 'pickles/' + op_name + '.pkl')#"time_prediction_v5/pickles/" + op_name +'.pkl'
        with open(filename, "rb") as f:
            reg = pickle.load(f)
        regressions [op_name] = reg

    for param in tf.operations [op_name].op_dict.keys ():
        print ("Param:", param)
        param_vals [param] = tf.operations [op_name].op_dict [param]['getter'] (graph, node)
        print (param, param_vals[param])
    surrogate_model = regressions[op_name]
    paramsList = []
    for key, value in param_vals.items():
        paramsList.append (value)
    print ('params list', np.array (paramsList))
    time = surrogate_model.predict_values (np.array ([paramsList]))
    print (time)
    return time
