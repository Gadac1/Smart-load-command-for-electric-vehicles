import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
from house_load import *
from smart_command import *

Time_Day = np.linspace(1,24,24)
T_Sim = np.linspace(0, intervalle_temps, n_intervalles)

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

Delta_U_1_no_ev = (R1*active_house_load + X1*reactive_house_load)/V
Delta_U_2_no_ev = (R2*active_house_load + X2*reactive_house_load)/V
Delta_U_3_no_ev = (R3*active_house_load + X3*reactive_house_load)/V

Delta_U_1_ev_naif = (R1*(active_house_load+active_load_ev_naif) + X1*reactive_house_load)/V
Delta_U_2_ev_naif = (R2*(active_house_load+active_load_ev_naif) + X2*reactive_house_load)/V
Delta_U_3_ev_naif = (R3*(active_house_load+active_load_ev_naif)+ X3*reactive_house_load)/V

Delta_U_1_ev_smart = (R1*(active_house_load+active_load_ev_smart) + X1*reactive_house_load)/V
Delta_U_2_ev_smart = (R2*(active_house_load+active_load_ev_smart) + X2*reactive_house_load)/V
Delta_U_3_ev_smart = (R3*(active_house_load+active_load_ev_smart)+ X3*reactive_house_load)/V

I_no_ev = apparent_house_load/V
I_ev_naif = (active_house_load + active_load_ev_naif)/(V*0.8)
I_ev_smart = (active_house_load + active_load_ev_smart)/(V*0.8)

### Affichage
## Diagramme du planning de charge
# Define colormap

cmapmine = ListedColormap(['w', 'b'], N=2)

# Plot matrix

fig, ax1 = plt.subplots(1)
ax1.imshow(table_charge_opti, cmap=cmapmine, vmin=0, vmax=1)
ax1.set_title('Répartition de charge dans le temps (temps en unité de delta_t)')

plt.show()

## Appel de puissance réactive en fonction du temps pour les VE

plt.plot(T_Sim, puissance_smart,'b')
plt.plot(T_Sim, puissance_naive,'g')
plt.title("Appel de puissance réactive pour le chargement de VE avec et sans optimisation")
plt.xlabel("Temps")
plt.ylabel("Puissance (W)")
plt.legend(("Chargement Smart","Chargement Naif"))
plt.ylim(0, p_ev*n_ev*1.05)
plt.show()

## Appel de puissance réactive totale

plt.plot(Time_Day, active_house_load,'r')
plt.plot(Time_Day, active_house_load+active_load_ev_naif,'g')
plt.plot(Time_Day, active_house_load+active_load_ev_smart,'b')
plt.title("Appel de puissance réactive total")
plt.xlabel("Temps")
plt.ylabel("Puissance (W)")
plt.legend(("Chargement Naif","Chargement Smart"))
plt.show()

## Affichage DeltaV
plt.plot(Time_Day, Delta_U_1_no_ev, 'r')
plt.plot(Time_Day, Delta_U_2_no_ev, 'r')
plt.plot(Time_Day, Delta_U_3_no_ev, 'r')
plt.plot(Time_Day, Delta_U_1_ev_naif, 'g')
plt.plot(Time_Day, Delta_U_2_ev_naif, 'g')
plt.plot(Time_Day, Delta_U_3_ev_naif, 'g')
plt.plot(Time_Day, Delta_U_1_ev_smart, 'b')
plt.plot(Time_Day, Delta_U_2_ev_smart, 'b')
plt.plot(Time_Day, Delta_U_3_ev_smart, 'b')
plt.title("Chute de tension dans les trois branches sans EV")
plt.xlabel("Temps")
plt.ylabel("Volt (V)")
plt.show()

## Affichage Courant

plt.plot(Time_Day,I_no_ev,'r')
plt.plot(Time_Day,I_ev_naif,'g')
plt.plot(Time_Day,I_ev_smart,'b')
plt.title("Appel de courant sur les cables")
plt.xlabel("Temps")
plt.ylabel("Courant (A)")
plt.legend(("Sans VE","Avec stratégie naive", "Avec stratégie smart"))
plt.show()
### load display to export to simulink

print((np.divide(230**2,active_house_load)).tolist())
print((np.divide(230**2,reactive_house_load*2*np.pi*50)).tolist())
print((np.divide(230**2,active_load_ev_naif)).tolist())
print((np.divide(230**2,active_load_ev_smart)).tolist())
