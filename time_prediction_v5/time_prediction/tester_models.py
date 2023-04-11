from csdl import Model
import numpy as np
import csdl
import scipy

class AddTester (Model):
    def define(self):
        num_elements = 11222
        num_iter = 400
        a = self.declare_variable ('a', val = np.random.rand (num_elements))
        b = self.declare_variable ('b', val = np.random.rand (num_elements))
        # c = self.declare_variable ('c', val = np.random.rand (1))
        for i in range (num_iter):
            self.register_output (str(i), a+b)

class PNormTester (Model):
    def initialize(self):
        self.parameters.declare ('num_elements')
    def define(self):
        num_elements = self.parameters['num_elements']
        num_iter = 400
        a = self.declare_variable ('a', val = np.ones ((num_elements)))
        print ("A: ", a)
        # c = self.declare_variable ('c', val = np.random.rand (1))
        for i in range (num_iter):
            self.register_output (str(i), csdl.pnorm (a, axis = (0), pnorm_type=2)) #ERROR HERE

            
class SumTester (Model):
    def initialize(self):
        self.parameters.declare ('params')
    def define(self):
        params = self.parameters ['params']
        num_iter = 256
        csdl_params = []
        for i, arr in enumerate (params):
            csdl_params.append (self.create_input (str(i) + "_input", arr))
        for i in range (num_iter):
            self.register_output(str(i) + "_output", csdl.sum(*csdl_params)) # * unpacks the tuple/list

class MatVecTester (Model):
    def define (self):
        mat = self.create_input ('mat', np.random.rand (2000, 2001))
        mat2 = self.create_input ('mat2', np.random.rand (2000, 2001))
        vec = self.create_input ('vec', np.random.rand (2001))
        add = mat+mat2
        for i in range (284):
            self.register_output (str (i), csdl.matvec (add, vec))

class SparseMatVecTester (Model):
    def define (self):
        
        vec = self.create_input ('vec', np.ones ((5000)))
        for i in range (9):
            self.register_output (str(i), csdl.matvec (scipy.sparse.random(5000, 5000, 4 * 0.01, format='csr'), vec))
class MatMatTester (Model):
    def define (self):
        mat = self.create_input ('mat1', np.random.rand (263, 82))
        vec = self.create_input ('mat2', np.random.rand (82, 132))
        for i in range (284):
            self.register_output (str (i), csdl.matmat (mat, vec))
class CrossTester (Model):
    def define (self):
        vec1 = self.create_input ('vec1', np.random.rand (3))
        vec2 = self.create_input ('vec1', np.random.rand (3))
        for i in range (500):
            self.register_output (str (i), csdl.cross (vec1, vec2, axis = 0))
class completeTester (Model):
    def define (self):
        num_iter = 1000
        for i in range (num_iter):
            arr1 = self.declare_variable (str(i) + 'arr1', np.random.rand (200, 200))
            arr2 = self.declare_variable (str(i) + 'arr2', np.random.rand (200, 200))
            vec1 = self.declare_variable (str(i) + 'vec1', np.random.rand (200))
            vec2 = vec1 *5
            arr4 = self.register_output (str(i) + 'arr4', arr1+arr2)
            arr5 = csdl.tanh (arr4) + arr1 - arr2
            arr6 = self.register_output (str(i) + 'arr6', arr4 + arr5)
            self.register_output (str(i) + 'arr7', csdl.matvec (arr6, vec1))

class tanhSum (Model):
    def define (self):
        num_iter = 1000
        for i in range (num_iter):
            arr1 = self.declare_variable (str(i) + 'arr1', np.random.rand (200))
            arr2 = self.declare_variable (str(i) + 'arr2', np.random.rand (200))
            vec1 = self.declare_variable (str(i) + 'vec1', np.random.rand (200))
            arr5 = csdl.sum (csdl.tanh (arr1), arr1, arr2)
            self.register_output (str(i), arr5)

class eoioTester (Model):
    def define (self):
        num_iter = 1000
        for i in range (num_iter):
            arr1 = self.declare_variable (str(i), np.random.rand (200))
            arr2 = self.declare_variable (str (i)+'arr2', np.random.rand (200))
            self.register_output ('sum' + str(i), csdl.sum (arr1, arr2))

class single_mins (Model):
    def define (self):
        num_iter = 3295
        for i in range (num_iter):
            arr1 = self.declare_variable (str(i), np.random.rand (20000))
            self.register_output ('sum' + str(i), csdl.min (arr1))

class double_mins (Model):
    def define (self):
        num_iter = 3295
        for i in range (num_iter):
            arr1 = self.declare_variable (str(i), np.random.rand (20000))
            self.register_output ('sum' + str(i), csdl.min (arr1, arr1*1))