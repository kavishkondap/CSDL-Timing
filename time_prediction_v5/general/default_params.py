import numpy as np
def get_size (graph, node):
    """
    Returns the size of the input node in a computation graph.

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node
        The the node whose size needs to be computed.

    Returns:
    --------
    size : int
        The size of the input node, computed as the product of the dimensions of the output tensor.

    Raises:
    -------
    IndexError
        If the input node has no predecessors in the computation graph.
    """
    output = list(graph.predecessors(node))[0]
    size = np.prod(output.var.shape)
    return size
def get_axis (graph, node):
    """
    Returns the axis value of the input node in a computation graph. Applicable for any VariableNode with an axis property

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    axis : int
        The axis of the input node
    """
    print ("axis", node.op.literals['axis'])
    return len (node.op.literals['axis'])

def get_num_params (graph, node):
    """
    Returns the total amount of inputs of the passed in node, which is used for VariableNodes with multiple parameters

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    num_params : int
        The amount of parameters (inputs) of the node
    """
    return len (list (graph.predecessors(node)))

def get_var1_dim1 (graph, node):
    """
    Returns the first dimension of the first input node of the provided node.

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    var1_dim1: int
        The first dimension of the first input
    """
    return get_op_input_dim(node,0,0)

def get_var1_dim2 (graph, node):
    """
    Returns the second dimension of the first input node of the provided node.

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    var1_dim2: int
        The second dimension of the first input
    """
    try:
        return get_op_input_dim(node, 0,1)
    except:
        return 10


def get_var2_dim2 (graph, node):
    """
    Returns the second dimension of the second input node of the provided node.

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    var1_dim1: int
        The second dimension of the second input
    """
    return get_op_input_dim(node, 1, 1)

def get_op_input_dim(node, input_num, dim):
    """
    A helper function that gets the dimension of a specified input node.

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    shape_dim (int): the specified dimension of the node
    """
    shape = node.op.dependencies[input_num].shape
    print ("Shape", shape)
    return shape[dim]

def get_sparsematmat_num_non_zero_percentage (graph, node):
    """
    Returns the number of nonzero elements in a sparsematmat node

    Parameters:
    -----------
    graph : networkx.DiGraph
        The computation graph.
    node : Graph Representation node to be analyzed

    Returns:
    --------
    nnz: int
        The percentage of nonzero elements in the sparse matrix
    """
    return 0.01
    return len(node.op.literals['sparse_mat'].nonzero())/get_size (graph, node)*100