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
    0.666666666666667,
    0.583333333333333,
    0.695833333333333,
    0.737500000000000,
    0.666666666666667,
    0.583333333333333,
    0.777777777777777,
    1,
    0.979166666666667,
    0.958333333333333,
    0.937500000000000,
    0.916666666666667,
    0.875000000000000,
    0.750000000000000,
    0.666666666666667])

max_load = 48000 #W per hamlet

apparent_house_load = max_load * pu
active_house_load = max_load * pu * 0.8
reactive_house_load = max_load * pu * 0.6
