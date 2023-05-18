# def nested_loops(data, level=0):
#     # base case
#     if level == len(data):
#         print("End")
#         return

#     for i in range(data[level]["start"], data[level]["end"]):
#         print(f"Level {level}: {i}")
#         nested_loops(data, level + 1)

# data = [{"start": 0, "end": 2}, {"start": 9, "end": 12}, {"start": 20, "end": 22}]
# nested_loops(data)

# thing = [1, 2]
# arr = [1, 2, 3, 4, 5]

# NUM_ITERS = {
#         "linear_combination": 512,
#         'power_combination':512,
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
# #         'log10':512,
# #         'cross':256,
# #         'dot':1024,
# #         'inner':1024,
# #         'outer':128,
# #         'exp_a':256,
# #         'rotmat':256,
# #         'min_singular':256,
# #         'max_singular':256,
# #         'average_singular':256,
# #         'min_multiple':256,
# #         'max_multiple':256,
# #         'average_multiple':256,
# # }

# # print (type (NUM_ITERS.keys ()))

# from python_csdl_backend import Simulator
# import numpy as np
# from csdl import Model
# import csdl
# import time
# import pandas as pd
# import openpyxl
# from csdl import StandardOperation
# from csdl.operations.exp import exp
# from csdl.operations.log import log
# from csdl.operations.log10 import log10
# from csdl.operations.sin import sin
# from csdl.operations.cos import cos
# from csdl.operations.tan import tan
# from csdl.operations.cosec import cosec
# from csdl.operations.sec import sec
# from csdl.operations.cotan import cotan
# from csdl.operations.cosech import cosech
# from csdl.operations.sech import sech
# from csdl.operations.cotanh import cotanh
# from csdl.operations.arcsin import arcsin
# from csdl.operations.arccos import arccos
# from csdl.operations.arctan import arctan
# # from csdl.operations.uq_tile import uq_tile
# # from csdl_om.comps.uq_tilecomp import UQTile

# # from csdl.operations.arccosec import arccosec
# # from csdl.operations.arcsec import arcsec
# # from csdl.operations.arccotan import arccotan
# from csdl.operations.sinh import sinh
# from csdl.operations.cosh import cosh
# from csdl.operations.tanh import tanh
# from csdl.operations.arcsinh import arcsinh
# from csdl.operations.arccosh import arccosh
# from csdl.operations.arctanh import arctanh
# from csdl.operations.linear_combination import linear_combination
# from csdl.operations.power_combination import power_combination
# from csdl.operations.passthrough import passthrough # No clue
# from csdl.operations.print_var import print_var # NOT NEEDED
# from csdl.operations.indexed_passthrough import indexed_passthrough # y = x[2]
# from csdl.operations.decompose import decompose # 
# # from csdl.operations.combined import combined NOT NEEDED
# from csdl.operations.matmat import matmat
# from csdl.operations.matvec import matvec
# from csdl.operations.pnorm import pnorm
# from csdl.operations.transpose import transpose
# from csdl.operations.inner import inner
# from csdl.operations.outer import outer
# from csdl.operations.dot import dot
# from csdl.operations.cross import cross
# from csdl.operations.einsum import einsum
# from csdl.operations.rotmat import rotmat
# from csdl.operations.expand import expand
# from csdl.operations.reshape import reshape
# from csdl.operations.reorder_axes import reorder_axes
# from csdl.operations.sum import sum
# from csdl.operations.average import average
# from csdl.operations.min import min
# from csdl.operations.max import max

# from scipy.sparse import csr_matrix

# class LinearCombination (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         b = self.declare_variable ('b', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), a+b)
# class Multiplication_PowerCombination (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         b = self.declare_variable ('b', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), 2*a)
# class Exponential_PowerCombination (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         b = self.declare_variable ('b', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), a**2)
# class Sin (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.sin (a))
# class Cos (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.cos (a))
# class Tan (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.tan (a))
# class Sec (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.sec (a))
# class Cosec (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.cosec (a))
# class Cotan (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.cotan (a))
# class Arcsin (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.arcsin (a))
# class Arccos (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.arccos (a))
# class Arctan (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.arctan (a))
# class Arcsin (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.arcsin (a))
# class Arccos (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.arccos (a))
# class Arctan (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.arctan (a))
# class Sec (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.sec (a))
# class Cosec (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.cosec (a))
# class Cotan (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.cotan (a))
# class Cosech (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.cosech (a))
# class Sech (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.sech (a))
# class Cotanh (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.cotanh (a))
# class Sinh (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.sinh (a))
# class Cosh (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.cosh (a))
# class Tanh (Model):
#         def initialize (self):
#                 self.parameters.declare ('num_iter')
#                 self.parameters.declare ('size')
#         def define(self):
#                 num_iter = self.parameters ['num_iter']
#                 size = self.parameters ['size']
#                 a = self.declare_variable ('a', val = np.ones ((size)))
#                 for i in range (num_iter):
#                         self.register_output (str(i), csdl.tanh (a))
# class Exp (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.exp(a))
# class PNorm (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#         self.parameters.declare ('axes')
#         self.parameters.declare ('arr')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         axes = self.parameters ['axes']
#         arr = self.parameters['arr']
#         a = self.declare_variable ('a', val = arr)
#         # b = self.declare_variable ('b', val = np.ones ((num_elements)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.pnorm (a, axis = axes, pnorm_type=2))
# class Sum (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('params')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         params = self.parameters ['params']
#         csdl_params = []
#         for i, arr in enumerate (params):
#             csdl_params.append (self.create_input (str(i) + "_input", arr))
#         for i in range (num_iter):
#             self.register_output(str(i) + "_output", csdl.sum(*csdl_params)) # * unpacks the tuple/list
# class MatVec (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('width')
#         self.parameters.declare ('height')
#     def define(self):
#         num_iter = self.parameters['num_iter']
#         width = self.parameters ['width']
#         height = self.parameters['height']

#         mat = self.create_input ('mat', np.ones((width, height)))
#         vec = self.create_input ('vec', np.ones ((height)))

#         # Creating the output for matrix-vector multiplication
#         for i in range (num_iter):
#             self.register_output(str(i), csdl.matvec(mat, vec))
# class Reshape (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#         self.parameters.declare ('shape')
#     def define (self):
#         num_iter = self.parameters['num_iter']
#         size = self.parameters ['size']
#         shape = self.parameters['shape']
#         arr = self.create_input ('arr_input', np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str (i), csdl.reshape (arr, shape))

# class MatMat (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('dim1')
#         self.parameters.declare ('dim2')
#         self.parameters.declare ('dim3')
#     def define(self):
#         num_iter = self.parameters['num_iter']
#         dim1 = self.parameters ['dim1']
#         dim2 = self.parameters['dim2']
#         dim3 = self.parameters ['dim3']

#         mat1 = self.create_input ('mat1', np.ones((dim1, dim2)))
#         mat2 = self.create_input ('mat2', np.ones ((dim2, dim3)))
#         # Creating the output for matrix-matrix multiplication
#         for i in range (num_iter):
#             self.register_output(str(i), csdl.matmat(mat1, mat2))
    
# class SparseMatMat (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('mat')
#         self.parameters.declare ('sparsemat')
#     def define(self):
#         num_iter = self.parameters['num_iter']
#         mat = self.create_input ('mat', self.parameters ['mat'])
#         # sparse_mat = self.create_input ('sparse_mat', )
#         # Creating the output for matrix-matrix multiplication
#         for i in range (num_iter):
#             self.register_output(str(i), csdl.sparsematmat(mat, sparse_mat=self.parameters['sparsemat']))
# class Log (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.log(a))

# class Log10 (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.log10(a))

# class Cross (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#     def define (self):
#         num_iter = self.parameters['num_iter']
#         a = self.declare_variable ('a', val = np.ones ((3)))
#         b = self.declare_variable ('b', val = np.ones ((3)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.cross(a, b, axis=0))

# class Dot (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         b = self.declare_variable ('b', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.dot(a, b))

# class Inner (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         b = self.declare_variable ('b', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.inner(a, b))

# class Outer (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size1')
#         self.parameters.declare ('size2')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size1 = self.parameters ['size1']
#         size2 = self.parameters ['size2']
#         a = self.declare_variable ('a', val = np.ones ((size1)))
#         b = self.declare_variable ('b', val = np.ones ((size2)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.outer(a, b))

# class Exp_a (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         x = self.declare_variable ('x', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.exp_a(1, x))

# class Rotmat (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#         self.parameters.declare ('axis')
#     def define(self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         axis = self.parameters ['axis']
#         angles = self.declare_variable ('angles', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.rotmat(angles, axis=axis))

# class Min_Singular (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.min(a))

# class Max_Singular (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.max(a))

# class Average_Singular (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.average(a))

# class Min_Multiple (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('params')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         params = self.parameters ['params']
#         csdl_params = []
#         for i, arr in enumerate (params):
#             csdl_params.append (self.create_input (str(i) + "_input", arr))
#         for i in range (num_iter):
#             self.register_output(str(i) + "_output", csdl.min(*csdl_params))

# class Max_Multiple (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('params')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         params = self.parameters ['params']
#         csdl_params = []
#         for i, arr in enumerate (params):
#             csdl_params.append (self.create_input (str(i) + "_input", arr))
#         for i in range (num_iter):
#             self.register_output(str(i) + "_output", csdl.max(*csdl_params))


# class Average_Multiple (Model):
#     def initialize (self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('params')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         params = self.parameters ['params']
#         csdl_params = []
#         for i, arr in enumerate (params):
#             csdl_params.append (self.create_input (str(i) + "_input", arr))
#         for i in range (num_iter):
#             self.register_output(str(i) + "_output", csdl.average(*csdl_params))

# min_mult

# from time_prediction_v3.general.default_params import get_size, get_num_params
# from csdl import Model
# import csdl
# import numpy as np

# scale_factor = 2
# size_list = [scale_factor**size_iter for size_iter in range (1, 13)]
# num_params_
# # scale_factor = 2
# # for size_iter in range (1, 13):
# #     size_list.append (scale_factor**size_iter)

# op_dict = {"source_node":min
#             'size':{
#                         "vals":size_list,
#                         "getter": get_size},
#             'num_params'{
#                         "vals":
#                         "getter":get_num_params
#             }
#             }

# class DataCollector (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#         self.parameters.declare ('num_params')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         num_params = self.parameters ['num_params']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.min (*np.repeat (a, num_params)))

# # min_sing

# from time_prediction_v3.general.default_params import get_size
# from csdl import Model
# import csdl
# import numpy as np

# scale_factor = 2
# size_list = [scale_factor**size_iter for size_iter in range (1, 13)]

# # scale_factor = 2
# # for size_iter in range (1, 13):
# #     size_list.append (scale_factor**size_iter)

# op_dict = {'size':{
#                         "vals":size_list,
#                         "getter": get_size},
#             }

# class DataCollector (Model):
#     def initialize(self):
#         self.parameters.declare ('num_iter')
#         self.parameters.declare ('size')
#     def define (self):
#         num_iter = self.parameters ['num_iter']
#         size = self.parameters ['size']
#         a = self.declare_variable ('a', val = np.ones ((size)))
#         for i in range (num_iter):
#             self.register_output (str(i), csdl.min(a))

# #min


# Min:{
# “op_getter”: get_max_node
# 	“params”:{
# “size”:get_size,
# “num_params”:num_params
# 		}
# op_dict = {"op_getter":get_min_node,
#            "params": {"size":get_size}}

# PLOTTING HERE *****************************************************************************************************

# from time_prediction_v3.time_prediction.plot_regression import plot_regression_3d
# import pickle
# import numpy as np
# from smt.surrogate_models import KRG, RMTB
# from time_prediction_v3.time_prediction.plot_regression import plot_regression_2d
# import pandas as pd
# # import matplotlib.pyplot as plt

# def regression (data, cols):
#     xt = np.zeros ((len (data['times']), len (cols))) # creates an array for the regression params, with rows for time, and the values that made that time 
#     for i in range (len (data['times'])):
#         vals = []
#         for j in range (len (cols)):
#             vals.append (data[cols[j]][i])
#         # print ("VALS: ", vals)
#         xt[i,:] = np.array (vals)
#     # xt = data['size'].to_numpy ()
#     yt = np.array (data ['times'])
#     xlimits = []
#     for i in range (len (xt[0])):
#         xlimits.append ([xt[0][i], xt[-1][i]])
#     interp = RMTB(print_global = False, num_ctrl_pts=20, nonlinear_maxiter=100, xlimits = np.array (xlimits))
#     interp.set_training_values(xt, yt)
#     interp.train()
#     # print ("PLOTTING REGRESSION")
#     # plot_regression_3d (xt, yt, interp)
#     return (xt, interp)

# filename = "time_prediction_v5/pickles/min_singular.pkl"
# with open(filename, "rb") as f:
#     reg = pickle.load(f)

# data = pd.read_csv ('time_prediction_v5/data/min_singular.csv')
# cols = list (data.keys ())[1:-1]
# print (cols)
# reg = regression (data, cols)
# fig = plot_regression_2d (reg[0], reg[1])
# # fig.show ()

# # PLOTTING ENDS HERE *****************************************************
# from csdl import Model, GraphRepresentation
# import csdl
# import numpy as np
# from csdl.rep.operation_node import OperationNode

# class mult (Model):
#     def define (self):
#         num_iter = 1
#         for i in range (num_iter):
#             arr1 = self.declare_variable (str(i), np.random.rand (20000))
#             arr2 = self.declare_variable (str(i), np.random.rand (20000))
#             self.register_output ('sum' + str(i), arr1*arr2)

# class exp (Model):
#     def define (self):
#         num_iter = 1
#         for i in range (num_iter):
#             arr1 = self.declare_variable (str(i), np.random.rand (20000))
#             arr2 = self.declare_variable (str(i), np.random.rand (20000))
#             self.register_output ('sum' + str(i), arr1**arr2)

# class constexp (Model):
#     def define (self):
#         num_iter = 1
#         for i in range (num_iter):
#             arr1 = self.declare_variable (str(i), np.random.rand (20000))
#             arr2 = self.declare_variable (str(i), np.random.rand (20000))
#             self.register_output ('sum' + str(i), arr1*arr2**2)

# class constbase (Model):
#     def define (self):
#         num_iter = 1
#         for i in range (num_iter):
#             arr1 = self.declare_variable (str(i), np.random.rand (20000))
#             arr2 = self.declare_variable (str(i), np.random.rand (20000))
#             self.register_output ('sum' + str(i), 2**arr1)
# model = constexp ()
# rep = GraphRepresentation(model)
# graph = rep.flat_graph
# for node in graph:
#     if isinstance (node, OperationNode):
#         op_name = str(node.op).split ()[0].split('.')[-1]
#         print (op_name)
# import scipy.sparse
# dim1 = 1000
# dim2 = 1000
# nnz = 5
# arr = scipy.sparse.random(dim1, dim2, nnz * 0.01, format='csr')
# print (arr.shape)

import numpy as np

# # 50 points

# # 

# choices = np.repeat ((5), 5)
# print (choices)
# scores = np.zeros ((5))
# sum = choices.sum ()
# for i in range (5):
#     scores[i] = (50-sum) * choices[i]
# print (scores)
import numpy as np
import matplotlib.pyplot as plt
mass = 1
k = 4.38649
init_pos = 1
init_vel = 0
delta_t = 0.02
init_time = 0

def pos (x_nought, vel, acc, delta_t):
    return x_nought + vel*delta_t + 1/2*acc*(delta_t)**2
def vel (vel_nought, delta_t, acc):
    return vel_nought + acc*delta_t
def acc (mass, pos, k):
    return -pos*k/mass
def time (time, delta_t):
    return time+delta_t

pos_list = [init_pos]
vel_list = [init_vel]
acc_list = [acc (mass, init_pos, k)]
time_list = [init_time]

while time_list[-1]<13:
    new_time = time (time_list[-1], delta_t)
    new_pos = pos (pos_list[-1], vel_list[-1], acc_list [-1], delta_t)
    new_vel = vel (vel_list[-1], delta_t, acc_list [-1])
    new_acc = acc (mass, pos_list [-1], k)

    pos_list.append (new_pos)
    vel_list.append (new_vel)
    acc_list.append (new_acc)
    time_list.append (new_time)

print (time_list)
print (pos_list)
print (vel_list)
print (acc_list)

plt.scatter (time_list, pos_list, color = 'r')
plt.scatter (time_list, vel_list, color = 'g')
plt.scatter (time_list, acc_list, color = 'b')
plt.show ()