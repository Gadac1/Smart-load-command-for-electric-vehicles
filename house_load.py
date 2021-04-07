import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

pu = np.array([0.625000000000000,
    0.583333333333333,
    0.562500000000000,
    0.541666666666667,
    0.516666666666667,
    0.562500000000000,
    0.583333333333333,
    0.666666666666667,
    0.750000000000000,
    0.833333333333333,
    0.875000000000000,
    0.895833333333333,
    0.937500000000000,
    0.958333333333333,
    0.968750000000000,
    0.979166666666667,
    1,
    0.979166666666667,
    0.958333333333333,
    0.937500000000000,
    0.916666666666667,
    0.875000000000000,
    0.750000000000000,
    0.666666666666667])

nominal_load = 48000 #W per hamlet
T = np.linspace(1,24,24)

active_load = nominal_load * pu * 0.8
reactive_load = nominal_load * pu * 0.6

# plt.plot(T,active_load)
# plt.plot(T,reactive_load)
# plt.show()