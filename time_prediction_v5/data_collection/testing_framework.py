from time_prediction_v5.general.helper import filterOps
from time_prediction_v5.data_collection.operation import Operation
from time_prediction_v5.data_collection.time_operation import timeOperation
from time_prediction_v5.time_prediction.surrogate_saver import surrogate_saver
import pandas as pd
from pkg_resources import resource_filename

class TestingFramework ():
    
    def __init__ (self):
        # self.master_dict = {}
        # self.num_iters = {}
        self.operations = {}
    def add_operation (self, op:Operation):
    # check to make sure that Operation is correct
    # make sure that self.func isn't None, operation.source_node exists in the CSDL library
    # make sure that args op_dict isn't empty
    # make sure that the operation isn't already in master_dict
        # self.master_dict [op.op_name] = op.op_dict
        # self.num_iters [op.op_name] = op.num_iter
        self.operations [op.op_name] = op

    def get_source_nodes (self):
        source_nodes = {}
        for op in self.operations.values ():
            if op.source_node in source_nodes:
                source_nodes [op.source_node].append (op.op_name)
            else:
                source_nodes [op.source_node] = [op.op_name]
        return source_nodes
    
    # def retrain_sm (self, to_include = 'all', sm_type = 'krg', save = True):


    def run (self, to_include = 'all', save = True):

        filtered_ops = filterOps (self.operations, to_include)
        for op in filtered_ops.values ():
            data = timeOperation(op)
            columns = ['num_iter', 'times']
            columns[1:1] = list (op.op_dict.keys ())
            df = pd.DataFrame (data, columns = columns)
            print ("DF MADE")
            if save:
                path = resource_filename('time_prediction_v5', "data/"+op.op_name+".csv")
                df.to_csv (path, index=False)
                surrogate_saver (df, op)
                # return None
            else:
                return df
            
# make it so you can retrain sm on preexisting data