import os
from fnmatch import fnmatch
from time_prediction_v5.general.constants import get_master_dict
from pkg_resources import resource_filename
from importlib import import_module

def attribute_tester (attr):
    root = resource_filename('time_prediction_v5', 'data_collection/operations')
    pattern = "*.py"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                # print (name)
                op = name [:-3]
                import_statement = os.path.join(path, name) [:-3].replace ('\\', '/').replace ('/', '.')
                import_statement = import_statement [import_statement.index ('time_prediction_v5'):]
                # print ("Import: ",  import_statement)
                try:
                    getattr(import_module(import_statement), attr)
                except:
                    assert False
    assert True

def test_op_checker ():
    path = resource_filename('time_prediction_v5', 'data_collection/operations/')
    pattern = "*.py"
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    for subfolder in subfolders:
        print (subfolder)
        files = os.listdir(subfolder)
        print (files)
        # for f in files:
        #     print (os.path.isfile (path+'\\'+f))
        files = [f for f in files if '.py' in f and '.pyc' not in f] 
        print (files)
        if (len (files)>=2):
            for file in files:
                import_statement = os.path.join(subfolder, file) [:-3].replace ('\\', '/').replace ('/', '.')
                import_statement = import_statement [import_statement.index ('time_prediction_v5'):]
                try:
                    getattr(import_module(import_statement), "op_checker")
                except:
                    assert False
    assert (True)

def test_data_collector ():
    attribute_tester ('DataCollector')

def test_op_dict ():
    attribute_tester ('op_dict')

def test_num_iter ():
    attribute_tester ('num_iter')