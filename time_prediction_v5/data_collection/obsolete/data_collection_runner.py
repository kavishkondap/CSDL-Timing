import numpy as np
import pandas as pd
from importlib import import_module
from time_prediction_v5.data_collection.time_operation import timeOperation
from time_prediction_v5.general.constants import get_master_dict
from time_prediction_v5.time_prediction.surrogate_saver import surrogate_saver
from time_prediction_v5.general.helper import filterDict
import os
from fnmatch import fnmatch
from pkg_resources import resource_filename

def data_collection_runner (keys_to_include, save=True):
    """
    Collects data on each operation passed in through the keys_to_include parameter using a prewritten file for each respective operation. 
    Recursively times each operation, and saves the data to a .csv file if save=True. Calls the surrogate_saver function to create and save a .pkl
    file using the Surrogate Modeling Toolbox.

    `Parameters`:
    - keys_to_include (str or list): defines the operations that will be timed by the function. If all need to be timed, pass in 'all'.
    Otherwise, pass in a list of which operations need to be timed (e.g. ['linear_combination', 'matmat', 'matvec'])
    - save (bool): Defaults to True. Defines whether or not the timing should be saved to .csv and .pkl files

    `Returns`:
    - No Return if save = True. If save = False, will return the Pandas DataFrame of the first operation passed into keys_to_include
  
    """
    master_dict = get_master_dict ()
    # print (master_dict)
    master_dict = filterDict (master_dict, keys_to_include)
    # print (master_dict)
    root = resource_filename('time_prediction_v5', 'data_collection/operations')
    pattern = "*.py"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                # print (name)
                op = name [:-3]
                if (op in master_dict):
                    import_statement = os.path.join(path, name) [:-3].replace ('\\', '/').replace ('/', '.')
                    import_statement = import_statement [import_statement.index ('time_prediction_v5'):]
                    # print ("Import: ",  import_statement)
                    try:
                        op_model = getattr(import_module(import_statement), "DataCollector")
                    except:
                        raise TypeError ("No module named ", import_statement, ". File must have an attribute named DataCollector")
                        # add errors EVERYWHERE and add unit tests
                    data = timeOperation (op_model, master_dict [op], op)
                    columns = ['num_iter', 'times']
                    columns[1:1] = list (master_dict[op].keys ())
                    df = pd.DataFrame (data, columns = columns)
                    print ("DF MADE")
                    if save:
                        path = resource_filename('time_prediction_v5', "data/"+op+".csv")
                        df.to_csv (path, index=False)
                        surrogate_saver (df, op, master_dict[op])
                        # return None
                    else:
                        return df

if __name__ == "__main__":
    data_collection_runner (['tanh'])
    # ['matmat', 'matvec', 'sum']