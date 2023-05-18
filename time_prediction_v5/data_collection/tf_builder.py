from time_prediction_v5.data_collection.testing_framework import TestingFramework
from time_prediction_v5.data_collection.operation import Operation
import scipy.sparse
import numpy as np
import csdl
from time_prediction_v5.general.default_params import get_size, get_var1_dim1, get_var1_dim2, get_var2_dim2, get_sparsematmat_num_non_zero_percentage, get_sparsematvec_num_non_zero_percentage, get_sparsematvec_dim1, get_sparsematvec_dim2, get_num_params

tf = TestingFramework ()

op = Operation('linear_combination', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (0, 1000000, 10000)], get_size)
op.add_argument('a', lambda size: np.ones ((size)))
op.add_argument('b', lambda size: np.ones((size)))
op.add_func(lambda a, b: a+b)
tf.add_operation(op)

op = Operation('matvec_sparse', num_iter=32)
op.add_parameter('dim1', range(1000, 10000, 2000), get_sparsematvec_dim1)
op.add_parameter('dim2', range(1000, 10000, 2000), get_sparsematvec_dim2)
op.add_parameter('nnz', range(1, 10, 2), get_sparsematvec_num_non_zero_percentage)
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

op = Operation('arccos', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('arcsin', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('arctan', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cos', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cosec', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cosech', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cosh', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cotan', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('cotanh', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('exp', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('exp_a', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('log', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('log10', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('matmat', num_iter=32)
op.add_parameter('dim1', range (100, 400, 50), get_var1_dim1)
op.add_parameter('dim2', range (100, 400, 50), get_var1_dim2)
op.add_parameter('dim3', range (100, 400, 50), get_var2_dim2)
op.add_argument('mtx1', lambda dim1, dim2, dim3: np.ones ((dim1, dim2)))
op.add_argument('mtx2', lambda dim1, dim2, dim3: np.ones(dim2, dim3))
op.add_func(lambda mtx1, mtx2: csdl.matmat(mtx1, mtx2))
# op.add_checker('matmat', lambda graph, node: node.op.literals ['sparsemtx'] is None)
tf.add_operation(op)

#matmat sparse: based on the nnz, and the dimensions of the nonsparse matrix



op = Operation('min_multiple', num_iter=256)
op.add_parameter('size', range (0, 25000, 10000), get_size)
op.add_parameter('num_params', range (2, 10), get_num_params)
op.add_argument('arr_list', lambda size, num_params: [np.ones ((size)) for i in range (num_params)])
op.add_func(lambda arr_list: csdl.min(*arr_list))
op.add_checker ('min', lambda graph, node: graph.in_degree (node)>1)
tf.add_operation(op)

op = Operation('min_singular', num_iter=256)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.min(arr))
op.add_checker ('min', lambda graph, node: graph.in_degree (node)==1)
tf.add_operation(op)

op = Operation('power_combination_exponent', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: arr**2)
op.add_checker ('power_combination', lambda graph, node: graph.in_degree (node)==1)
tf.add_operation(op)

op = Operation('power_combination_multiply', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr1', lambda size: np.ones ((size)))
op.add_argument('arr2', lambda size: np.ones ((size)))
op.add_func(lambda arr1, arr2: arr1*arr2)
op.add_checker ('power_combination', lambda graph, node: graph.in_degree (node)==2)
tf.add_operation(op)

op = Operation('sec', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('sech', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('sin', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('sinh', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('tan', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)

op = Operation('tanh', num_iter=512)
op.add_parameter('size', [i for i in range (100, 10000, 100)] + [i for i in range (10000, 1000000, 10000)], get_size)
op.add_argument('arr', lambda size: np.ones ((size)))
op.add_func(lambda arr: csdl.arccos(arr))
tf.add_operation(op)