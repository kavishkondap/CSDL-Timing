import numpy as np
import matplotlib.pyplot as plt

def plot_regression_2d (xt, interp):
    """
    A getter function that combines the num_iter variables defined in each operation-specific file into a dictionary.

    `Parameters`:
    - No parameters

    `Returns`:
    - returns the NUM_ITERS dictionary with the following structure:
        - NUM_ITERS = {  "linear_combination": 512, 'power_combination_multiply':512, 'power_combination_exponent':512, "pnorm": 512,...}
  
    """
    # xt = np.asarray ([i for i in range (0, 1000000, 1000)])
    yt = interp.predict_values (xt)
    print (np.asarray(xt).shape)
    print (np.asarray (yt).shape)
    plt.xlabel ("Size")
    plt.ylabel ("Time (Seconds)")
    plt.scatter(xt, yt)
    plt.show()

def plot_regression_3d (xt, interp):
    """
    Generates a 3D matplotlib graph of the given Surrogate Model and input range.

    `Parameters`:
    - xt

    `Returns`:
    - No Return
    """
    num_elements = []
    axes = []
    for x in xt:
        num_elements.append (x[0])
        axes.append (x[1])
    min_max_num_elements = (num_elements[0], num_elements[-1])
    min_max_axes = (axes[0], axes[-1])
    print ("MIN MAX NUM ELEMENTS: ", min_max_num_elements)
    print ("MIN MAX AXES: ", min_max_axes)
    num_elements_testing = np.linspace (min_max_num_elements[0], min_max_num_elements[1], 30)
    axes_testing = np.linspace (min_max_axes[0], min_max_axes[1], 30)
    params = []
    for i in num_elements_testing:
        for j in axes_testing:
            params.append ([i, j])
    
    times = interp.predict_values(np.array (params))
    for i in range (len (params)):
        params[i].append (times[i])
    timesFormatted = []
    num_elements_formatted = []
    axes_formatted = []
    for i in range (len (times)):
        timesFormatted.append (times[i][0])
        num_elements_formatted.append (params[i][0])
        axes_formatted.append (params [i][1])

    fig = plt.figure (figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    x_2d = []
    y_2d = []
    axis_constant = 1
    for i in range (len (num_elements_formatted)):
        if (axes_formatted[i]==axis_constant):
            x_2d.append (num_elements_formatted[i])
            y_2d.append (timesFormatted[i])
    # ax2.plot (x_2d, y_2d)
    # ax2.set_visible (True)
    X, Y, Z = np.meshgrid (num_elements_formatted, axes_formatted, timesFormatted)
    ax.plot_trisurf(num_elements_formatted, axes_formatted, timesFormatted, linewidth=0.2)
    ax.set_xlabel ("PARAM1")
    ax.set_ylabel ("PARAM2")
    ax.set_zlabel ("TIME")
    # ax.plot_surface(np.array (params))
    ax.set_visible(True)
    plt.show()