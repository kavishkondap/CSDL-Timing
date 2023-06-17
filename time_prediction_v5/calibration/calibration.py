from time_prediction_v5.data_collection.tf_builder import tf
import pandas as pd
import numpy as np
from pkg_resources import resource_filename

def partial_calibration ():
    """
    Rapid calibration for timing CSDL operations. Occurs by default upon installation of package,
    but can be recalibrated if desired.
  
    partial_calibration runs and times the linear_combination operation, and subsequently calculates the 
    ratio between the timing on a user's device and the reference timing for linear_combination from the package.
    This ratio is then saved, and multiplied by when providing results for a user's timing. Note the potential
    inaccuracy of using partial_calibration, as some operations may have incorrect timings. If more accurate timing is needed, use complete_calibration
  
    `Parameters`:
    - No Parameters

    `Returns`:
    - No Return
  
    """
    local_df = tf.run (to_include=['linear_combination'], save=False)
    path =  resource_filename('time_prediction_v5', 'data/linear_combination.csv')
    gen_df = pd.read_csv (path)
    ratios = []
    for i in range (len (local_df['times'])):
        ratios.append (local_df['times'][i]/gen_df['times'][i])
    ratios = np.asarray (ratios)
    avg_ratio = np.average (ratios)
    print (avg_ratio)
    std_dev = np.std (ratios)
    print (std_dev)
    path = resource_filename('time_prediction_v5', 'calibration/calibration_const.txt')
    with open(path, 'w') as f:
        f.write(str(avg_ratio))

def complete_calibration ():
    """
    Detailed  calibration for timing CSDL operations. Does not occur by default, must be manually executed by
    the user.
  
    complete_calibration runs and times all operations on a user's device, and saves both the .csv and .pkl files
    for surrogate models. These files are later referenced during timing, offering device-specific timing for CSDL models.
    Note this is a lengthy process, and may take multiple hours

    `Parameters`:
    - No Parameters

    `Returns`:
    - No Return
  
    """
    tf.run()
    path = resource_filename('time_prediction_v5', 'calibration/calibration_const.txt')
    with open(path, 'w') as f:
        f.write(str(1))