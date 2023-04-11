from smt.surrogate_models import KRG, RMTB
import pickle
import os
from time_prediction_v5.time_prediction.regression import regression
import pandas as pd
from pkg_resources import resource_filename
from time_prediction_v5.data_collection.operation import Operation

def surrogate_saver (df, op:Operation):
    """
    Saves the SMT regression for an operation as a .pkl file given the relevant data.

    Args:
        - df (Pandas DataFrame): a DataFrame with the data from a specific operation, including the times, and each parameter that produced that time
        - op_name (str) - The operation_type as a string (e.g. 'linear_combination', 'matvec')
        - op_dict (dict) - The operation dictionary that is defined within the operation-specific file.

    Returns:
        No return
    """
    params = list (op.op_dict.keys ())
    print (df.keys ())
    df ['times'] = df ['times']/df ['num_iter']
    del df ['num_iter']
    sm = regression (df, params)
    new_filename = resource_filename ("time_prediction_v5", "pickles/" + op.op_name + '.pkl')
    print (new_filename)
    with open(new_filename, "wb") as f:
        pickle.dump(sm, f)