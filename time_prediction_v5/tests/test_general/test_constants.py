import os
from time_prediction_v5.general.constants import get_master_dict, get_num_iters
from pkg_resources import resource_filename
from fnmatch import fnmatch

def test_get_master_dict ():
    dir_ops = []
    keys = list (get_master_dict ().keys ())
    root = resource_filename('time_prediction_v5', 'data_collection/operations')
    pattern = "*.py"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                dir_ops.append (name [:-3])
    # dir = os.listdir (resource_filename ('time_prediction_v5', 'data_collection/operations'))
    # dir_ops = []
    # for file in dir:
    #     if ('.py' in file):
    #         dir_ops.append (file [:-3])
    assert (sorted (keys)==sorted (dir_ops))

def test_get_num_iters ():
    dir_ops = []
    keys = list (get_num_iters ().keys ())
    root = resource_filename('time_prediction_v5', 'data_collection/operations')
    pattern = "*.py"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                dir_ops.append (name [:-3])
    # dir = os.listdir (resource_filename ('time_prediction_v5', 'data_collection/operations'))
    # dir_ops = []
    # for file in dir:
    #     if ('.py' in file):
    #         dir_ops.append (file [:-3])
    assert (sorted (keys)==sorted (dir_ops))

# def test_num_iter ():