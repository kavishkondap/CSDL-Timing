from python_csdl_backend import Simulator
import numpy as np
from csdl import Model, Variable, GraphRepresentation
from scipy.sparse import csr_matrix
from time_prediction_v5.general.helper import checkValidity, checkData
from time_prediction_v5.data_collection.data_collector import DataCollector
from time_prediction_v5.data_collection.operation import Operation

def timeOperation (op:Operation): #op_dict = the master dictionary for a specific operation, starting at the 2nd tier
    """
    Times the inputted CSDL model using multiple different parameters, which are found in the op_dict for a respective file.
    Calls the nested_loops function to recursively iterate through each parameter in
    the operation, as defined within the operation-specific file.


    `Parameters`:
    - model (CSDL Model) - The CSDL Model specifically written for a singular operation, located in the operation-specific file
    - op_dict (dict) - The operation dictionary that is defined within the operation-specific file.
    - op_type (str) - The operation_type as a string (e.g. 'linear_combination', 'matvec')

    `Returns`:
    - data (dict) - A dictionary that contains the timing data for the operation with the following structure:
        - data = {'num_iter':[...], str(param1): [...], str(param2): [...],..., 'times':[...]}
  
    """
    op_dict = op.op_dict
    keys = op_dict.keys ()
    data = {
        'num_iter':[],
        'times':[]
    }
    indicies = {
        'num_iter':None,
        'times':None
    }
    keys_dict = {}
    indicies = {}
    for i, key in enumerate (keys):
        data[str(key)] = []
        keys_dict [i] = str(key)
        indicies [str(key)] = None
    data = nested_loops (op, keys_dict, indicies, data)
    checkData (op_dict, data)
    return data

def nested_loops(op:Operation, keys_dict, indicies, data, level=0):
    """
    A recursive function that iterates through each parameter in the op_dict in a nested loop layout,
    and times the model with each permutation of values.


    `Parameters`:
    - op_dict (dict) - The operation dictionary that is defined within the operation-specific file.
    - keys_dict (dict) - A conversion dictionary that translates from the names of an operation parameter to a numerical index, which is used during the recursion
        - e.g. keys_dict = {0:'dim1', 1:'dim2'} for the matvec operation
    - indicies (dict) - A dictionary that contains the numerical values of each parameter, which are passed into the model. These values are updated each iteration to time different permutations of the model.
    - model (CSDL Model) - The CSDL Model specifically written for a singular operation, located in the operation-specific file
    - op_type (str) - The operation_type as a string (e.g. 'linear_combination', 'matvec')
    - data (dict) - A dictionary that contains the timing data for the operation, and is appended to after each iteration of nested_loops.

    `Returns`:
    - data (dict) - A dictionary that contains the timing data for the operation with the following structure:
        - data = {'num_iter':[...], str(param1): [...], str(param2): [...],..., 'times':[...]}
  
    """
    if level == len(op.op_dict.keys()):
# indicies.values ()
        # print (indicies.values ())
        args = []
        for arg in op.args:
            args.append ((arg[0] (*indicies.values ()), arg[1]))
        rep = GraphRepresentation (DataCollector(func = op.func, num_iter = op.num_iter, args = args))
        # print (indicies)
        checkValidity (op, rep)
        sim = Simulator(rep)
        t = sim.run()
        print (op.num_iter, indicies, t)
        data ['num_iter'].append (op.num_iter)
        data['times'].append (t)

        for i in keys_dict.keys ():
            data [keys_dict[i]].append (indicies[keys_dict[i]])
        return data
    for i in op.op_dict[keys_dict[level]]['values']:
        indicies [keys_dict[level]] = i
        data = nested_loops(op, keys_dict, indicies, data, level + 1)

        if (i == op.op_dict[keys_dict[level]]['values'][-1]):
            return data