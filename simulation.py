import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
from house_load import *
import main

V = 230 #V

r = 0.073 * 2 #Ohm/km
x = 0.08 * 2 #Ohm/km

length_branch1 = 189e-3 #km
length_branch2 = 213e-3 #km
length_branch3 = 218e-3 #km

R1 = length_branch1 * r
R2 = length_branch2 * r
R3 = length_branch3 * r

X1 = length_branch1 * x
X2 = length_branch2 * x
X3 = length_branch3 * x

U_1_no_ev = V - (R1*active_load + X1*reactive_load)/V
U_2_no_ev = V - (R2*active_load + X2*reactive_load)/V
U_3_no_ev = V - (R3*active_load + X3*reactive_load)/V
I = apparent_load/V

plt.plot(Time, U_1_no_ev)
plt.plot(Time, U_2_no_ev)
plt.plot(Time, U_3_no_ev)
plt.show()

plt.plot(Time,I)
plt.show()