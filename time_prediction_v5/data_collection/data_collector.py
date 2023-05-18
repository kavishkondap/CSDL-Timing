import csdl
from csdl import Model
import numpy as np

class DataCollector(Model):

    def initialize(self):
        self.parameters.declare('func')
        self.parameters.declare('num_iter', types=int)
        # self.parameters.declare('parameters_dict', types=dict)
        self.parameters.declare ('args', types=list)
    def define(self):
        func = self.parameters['func']
        num_iter = self.parameters['num_iter']
        args = self.parameters ['args']
        # print (np.asarray (args).shape)
        # print (args)
        for i, arg in enumerate (args):
            if (arg[1]): # arg is a tuple (value, csdl_variable = True/False)
                # print (i, arg[0])
                args [i] = self.declare_variable ("input_" + str(i), arg[0])
                # print (arg[0])
            else:
                args [i] = arg[0] #getting rid of the csdl_variable part of the args value, just keeping the variable itself
        # print (args)
        # parameters_dict = self.parameters['parameters_dict']

        # shapes = parameters_dict['shapes']

        # args = []
        # for ind, shape in enumerate(shapes):
        #     args.append(self.declare_variable(f'arg_{ind}', val=np.ones(shape)))

        for i in range(num_iter):
            # print (args)
            # print ("args", *args[:][0])
            # exit()
            val = func(*args)
            self.register_output("output_"+str(i), val)