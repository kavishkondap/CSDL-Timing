import os
from importlib import import_module
from fnmatch import fnmatch
from pkg_resources import resource_filename
# NUM_ITERS = {
#         "linear_combination": 512,
#         'power_combination_multiply':512,
#         'power_combination_exponent':512,
#         "pnorm": 512,
#         "sum":256,
#         'matvec':128,
#         'reshape':256,
#         'sin':512,
#         'cos':512,
#         'tan':512,
#         'arcsin':512,
#         'arccos':512,
#         'arctan':512,
#         'sec':512,
#         'cosec':512,
#         'cotan':512,
#         'cosech':512,
#         'sech':512,
#         'cotanh':512,
#         'sinh':512,
#         'cosh':512,
#         'tanh':512,
#         'matmat':32,
#         'sparsematmat':16,
#         'exp':512,
#         'log':512,
#         'log10':512,
#         'cross':256,
#         'dot':1024,
#         'inner':1024,
#         'outer':128,
#         'exp_a':256,
#         'rotmat':256,
#         'min_singular':256,
#         'max_singular':256,
#         'average_singular':256,
#         'min_multiple':256,
#         'max_multiple':256,
#         'average_multiple':256,
# }

# def get_num_iters ():
#     """
#     A getter function that combines the num_iter variables defined in each operation-specific file into a dictionary.

#     `Parameters`:
#     - No parameters

#     `Returns`:
#     - returns the NUM_ITERS dictionary with the following structure:
#         - NUM_ITERS = {  "linear_combination": 512, 'power_combination_multiply':512, 'power_combination_exponent':512, "pnorm": 512,...}
  
#     """
#     NUM_ITERS = {}
#     root = resource_filename ('time_prediction_v5', 'data_collection/operations/')
#     pattern = "*.py"

#     for path, subdirs, files in os.walk(root):
#         for name in files:
#             if fnmatch(name, pattern):
#                 import_statement = os.path.join(path, name) [:-3].replace ('\\', '/').replace ('/', '.')
#                 import_statement = import_statement [import_statement.index ('time_prediction_v5'):]
#                 op_num_iter = getattr(import_module(import_statement), "num_iter")
#                 NUM_ITERS [name[:-3]] = op_num_iter
#     return NUM_ITERS

# def get_master_dict ():
#     """
#     A getter function that combines the op_dict variables defined in each operation-specific file into a dictionary.
#     The function iterates through the files found in the time_prediction_v5/data_collection/operations directory to add
#     the op_dicts together.

#     `Parameters`:
#     - No parameters

#     `Returns`:
#     - returns the master_dictionary variable, which is a combination of the individual op_dicts from each operation file. 
  
#     """    
#     master_dictionary = {}
#     root = resource_filename ('time_prediction_v5', 'data_collection/operations/')
#     pattern = "*.py"
#     for path, subdirs, files in os.walk(root):
#         for name in files:
#             if fnmatch(name, pattern):
#                 # print (name)
#                 op = name [:-3]
#                 import_statement = os.path.join(path, name) [:-3].replace ('\\', '/').replace ('/', '.')
#                 import_statement = import_statement [import_statement.index ('time_prediction_v5'):]
#                 # print ("Import: ",  import_statement)
#                 op_dict = getattr(import_module(import_statement), "op_dict")
#                 master_dictionary[op] = op_dict
#                 # import_statement = "time_prediction_v3.data_collection.operations." + op + ""
#                 # print(os.path.join(path, name))
# # from time_prediction_v5.data_collection.operations.linear_combination.linear_combination import op_dict
#     # for op_file in op_dir:
#     #     if ('.py' in op_file):
#     #         op = op_file [:-3]
#     #         import_statement = "time_prediction_v3.data_collection.operations." + op
#     #         op_dict = getattr(import_module(import_statement), "op_dict")
#     #         master_dictionary[op] = op_dict
#     # print ("printing: ", master_dictionary)
#     return master_dictionary

# master_dictionry = {}
# for op_fil in directory:
#     from op_fil import master_dict_op
#     master_dictionry.update(master_dict_op)

# from lin_combo import lin_combo_dict

# master_dictionary = {

#     'linear_combination':{'size':get_size},
#     'power_combination':{'size':get_size},
#     'pnorm':{'size':get_size},
#     'sum':{'size':get_size},
#     'matvec':{'size':get_size},
#     'reshape':{'size':get_size},
#     'sin':{'size':get_size},
#     'cos':{'size':get_size},
#     'tan':{'size':get_size},
#     'arcsin':{'size':get_size},
#     'arccos':{'size':get_size},
#     'arctan':{'size':get_size},
#     'sec':{'size':get_size},
#     'cosec':{'size':get_size},
#     'cotan':{'size':get_size},
#     'cosech':{'size':get_size},
#     'sech':{'size':get_size},
#     'cotanh':{'size':get_size},
#     'sinh':{'size':get_size},
#     'cosh':{'size':get_size},
#     'tanh':{'size':get_size},
#     'matmat':{'size':get_size},
#     'sparsematmat':{'size':get_size},
#     'min_singular':{'size':get_size},
#     'max_singular':{'size':get_size},
#     'average_singular':{'size':get_size},
#     'min_multiple':{'size':get_size},
#     'max_multiple':{'size':get_size},
#     'average_multiple':{'size':get_size},
# }