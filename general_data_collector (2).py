import numpy as np
import csdl


class DataCollector(csdl.Model):

    def initialize(self):
        self.parameters.declare('func', types=function)
        self.parameters.declare('num_iter', types=int)
        self.parameters.declare('parameters_dict', types=dict)

    def define(self):
        func = self.parameters['func']
        num_iter = self.parameters['num_iter']
        parameters_dict = self.parameters['parameters_dict']

        shapes = parameters_dict['shapes']

        args = []
        for ind, shape in enumerate(shapes):
            args.append(self.declare_variable(f'arg_{ind}', val=np.ones(shape)))

        for ind in range(self.num_iter):
            self.register_output(str(ind), func(*args))


tf = TestingFramework(num_iter)

op = Operation('matvec_sparse', num_iter=num_iter)
op.add_parameter('nrow', range(1000, 10000, 2000))
op.add_parameter('ncol', range(1000, 10000, 2000))
op.add_parameter('nnz', range(1000, 10000, 2000))
op.add_argument('mtx', lambda a, b, nnz: scipy.sparse.random(a, b, nnz * 0.01, format='csr'), csdl_var=False)
op.add_argument('vec', lambda a, b, nnz: np.ones(b))
op.add_func(lambda mtx, vec: csdl.matvec(mtx, vec))
op.add_checker(lambda: None)
tf.add_operation(op)

tf.run()