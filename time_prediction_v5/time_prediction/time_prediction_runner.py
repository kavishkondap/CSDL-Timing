from time_prediction_v5.time_prediction.predict_time import predict_time
from time_prediction_v5.time_prediction.tester_models import MatVecTester, AddTester, completeTester, tanhSum, eoioTester, single_mins, double_mins, SparseMatVecTester
from csdl import Model, GraphRepresentation
from  python_csdl_backend import Simulator
import matplotlib.pyplot as plt
import numpy as np

model = SparseMatVecTester ()
rep = GraphRepresentation(model)
preds = []
emps = []
for i in range (1):
    prediction = predict_time (rep)
    sim = Simulator (model)
    empirical = sim.run ()
    # empirical = sim.run ()

    print ("Prediction: ", prediction)
    print ("Empirical: ", empirical)

    preds.append (prediction)
    emps.append (empirical)

x = np.array (preds+emps, dtype=object)
y = np.repeat (1, len (preds)+len (emps))
print (x.shape)
print (y.shape)
print (len (preds))
print (len (emps))
colors = list (np.repeat (10, len (preds))) + list (np.repeat (50, len (emps)))
# print (colors.shape)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, c=colors, alpha=0.5)
plt.show()
# plt.scatter ()
# percent_error = 