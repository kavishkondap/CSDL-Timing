from time_prediction_v5.data_collection.testing_framework import TestingFramework
from time_prediction_v5.data_collection.operation import Operation
import scipy.sparse
import numpy as np
import csdl
from time_prediction_v5.general.default_params import get_size, get_var1_dim1, get_var1_dim2, get_sparsematmat_num_non_zero_percentage

tf = TestingFramework ()

op = Operation('linear_combination', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (0, 1000000, 10000)], get_size)
op.add_argument('a', lambda size: np.ones ((size)))
op.add_argument('b', lambda size: np.ones((size)))
op.add_func(lambda a, b: a+b)
tf.add_operation(op)

op = Operation('matvec_sparse', num_iter=32)
op.add_parameter('dim1', range(1000, 10000, 2000), get_var1_dim1)
op.add_parameter('dim2', range(1000, 10000, 2000), get_var1_dim2)
op.add_parameter('nnz', range(1, 10, 2), get_sparsematmat_num_non_zero_percentage)
op.add_argument('mtx', lambda dim1, dim2, nnz: scipy.sparse.random(dim1, dim2, nnz * 0.01, format='csr'), csdl_var=False)
op.add_argument('vec', lambda dim1, dim2, nnz: np.ones(dim2))
op.add_func(lambda mtx, vec: csdl.matvec(mtx, vec))
op.add_checker('matvec', lambda graph, node: not node.op.literals ['sparsemtx'] is None)
tf.add_operation(op)

op = Operation('matvec_dense', num_iter=32)
op.add_parameter('dim1', range(250, 3000, 250), get_var1_dim1)
op.add_parameter('dim2', range(250, 3000, 250), get_var1_dim2)
op.add_argument('mtx', lambda dim1, dim2: np.ones ((dim1, dim2)))
op.add_argument('vec', lambda dim1, dim2: np.ones(dim2))
op.add_func(lambda mtx, vec: csdl.matvec(mtx, vec))
op.add_checker('matvec', lambda graph, node: node.op.literals ['sparsemtx'] is None)
tf.add_operation(op)