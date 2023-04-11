# **Adding New Operations - A Step By Step Guide**

## **Import Statements**
 ```python
from time_prediction_v5.general.default_params import ... # import the needed getter functions
from csdl import Model
import csdl
import numpy as np
```

## **Number of Iterations**

Set the number of iterations for the data collection using the variable name "num_iter". The num_iter value should be high enough that the times produced during data_collection are non_zero to ensure accurate results.
For less expensive operations, the num_iter can often be as high as 256 or 512, and can be as low as 32 or 64 for more costly operations.

Example:
```python
num_iter = 256 # variable name must be num_iter
```

## **Operation Dictionary**


Define the operation dictionary
Note, this variable must be named op_dict

Example:
```python
op_dict = {'dim1': {'values':dim1_list,
                    'getter': get_var1_dim1}
            'dim2': {'values':dim2_list
                    'getter': get_var1_dim2}} # variable name must be op_dict
```
In this example, the operation has parameters dim1 and dim2, with a 'values' and 'getter' for both.
You must define the list passed into the values key, preferably using the range of values that are expected to be found during the use of this operation

For instance, a size parameter for a linear_combination operation may have values defined as such:

```python
size = [i for i in range (100, 10000, 100)] + [i for i in range (0, 1000000, 10000)]
```

This list has the needed granularity for smaller values of size, while also reaching sizes near 1,000,000 to ensure accuracy for larger computations too

The 'getter' is how this property of the operation is accessed from the node in the graph. There exists a set of commonly used getters, each a function
that can be imported as "from time_prediction_v5.general.default_params import ..."

If none of these getters are compatible with the operation, a custom getter must be written in the operation file. For a custom getter, the function must have
inputs graph, node IN THAT ORDER for the function to work.

Example:
```python
def custom_getter (graph, node):
    #....
```
## **DataCollector CSDL Model**
Define a data collector CSDL model
Note, the model must be named DataCollector

Here is an example of a DataCollector model for linear_combination

```python
class DataCollector (Model):
    def initialize (self):
        # Declare the input parameters
        self.parameters.declare ('num_iter')
        self.parameters.declare ('size')
    def define(self):
        # Retrieve the input parameters
        num_iter = self.parameters ['num_iter']
        size = self.parameters ['size']
        
        # Declare variables using the defined parameters.
        a = self.declare_variable ('a', val = np.ones ((size)))
        b = self.declare_variable ('b', val = np.ones ((size)))
        
        # Perform the operation of interest for the specified number of iterations
        for i in range (num_iter):
            self.register_output (str(i), a+b)
```

## **Operation Checker**
The following information is only applicable to operations that require multiple datasets for different purposes. This issue arises due to 
the fact that some CSDL operations compute different things, or execute computations in a different manner depending on their inputs.

For instance, the csdl.min() operation, given a single matrix input, will find the minimum value of that matrix and return the scalar value.
However, for multiple matrix inputs, the csdl.min() operation will compute the element-wise minimum by comparing the matricies. These are two similar,
but differently executed operations wrapped within the single csdl.min () operation. Since the timing of both cannot exist in a single surrogate model,
two models must be defined, and thus, two (or more) files within the directory of that operation.

Building off of the example above with csdl.min(), we need a way to differentiate between a min operation with singular or multiple inputs,
and call the respective file. So, the function below determines the amount of inputs to the node, and returns a boolean value. The example shown
would be present in the min_singular file, since it returns True when only one input is present, and False otherwise.
```python
def op_checker (graph, node):
    if (graph.in_degree (node)==1):
        return True
    else:
        return False
```
Note that the op_checker function must take in graph, node IN THAT ORDER, otherwise an error will be produced. This function must return a boolean value.
ALL files in the operation directory must have an op_checker if multiple files are present.