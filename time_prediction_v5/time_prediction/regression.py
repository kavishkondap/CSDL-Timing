import numpy as np
from smt.surrogate_models import KRG
from time_prediction_v5.time_prediction.plot_regression import plot_regression_3d
def regression (data, params):
    """
    Uses the Surrogate Modeling Toolbox to take a Kriging regression of the provided data.

    Args:
    data (dict): the collected data for the operation, with times for each permutation of parameter values
    params (list): The parameter inputs for the operation

    Returns:
    interp: The trained surrogate model
    """
    xt = np.zeros ((len (data['times']), len (params))) # creates an array for the regression params, with rows for time, and the values that made that time 
    print (xt)
    print ((len (data['times']), len (params)))
    for i in range (len (data['times'])):
        vals = []
        for j in range (len (params)):
            vals.append (data[params[j]][i])
        xt[i,:] = np.array (vals)
    yt = np.array (data ['times'])
    print (xt)
    print (yt)
    interp = KRG(print_global = False)
    interp.set_training_values(xt, yt)
    interp.train()
    # print ("PLOTTING REGRESSION")
    # plot_regression_3d (xt, interp)
    return interp