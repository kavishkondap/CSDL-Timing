
class Operation ():

    def __init__(self, op_name, num_iter):
        self.args = []
        self.op_dict = {}
        self.func = None
        self.source_node = op_name
        self.checker = None
        self.op_name = op_name
        self.num_iter = num_iter

    def add_parameter (self, param_name:str, values, getter): #parameters are like size and nnz
        # param_dict = {}
        # op_dict.append (param_dict)
        self.op_dict [param_name] = {'values':list (values),
                                    'getter':getter}
        # ADD ERRORS HERE
        # if param name is already in op_dict --> ERROR
        # if param name isn't a string, values not a list/iterator --> ERROR
        # make sure getter is a function

    def add_argument (self, arg_name, arg_getter, csdl_var = True): #arguments are like the arrays actually passed into the function
        # self.args [arg_name] = {}
        self.args.append ((arg_getter, csdl_var))
        # MORE ERRORS HERE TOO
        # make sure arg_getter's a function, must take in the total number of parameters
    def add_func (self, func):
        self.func = func
        # check if function, else error
    def add_checker (self, source_node, checker):
        self.source_node = source_node
        self.checker = checker