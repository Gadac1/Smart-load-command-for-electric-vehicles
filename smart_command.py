import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random

intervalle_temps = 840 #Un intervalle global de charge en minutes (par exemple 360min pour une nuit de 8h)
delta_t = 10 #Un découpage temporel en minutes
n_intervalles = int(intervalle_temps/delta_t)
n_ev = 24 #Le nombre de véhicule électriques à simuler
p_ev = 6000 #W, l'appel de puissance de chaques véhicules

voit = []
table_naive = np.zeros((n_ev,n_intervalles))
T = np.linspace(0, intervalle_temps, n_intervalles)

class Voiture:
    def __init__(self, load_time, load_start, P):
        self.load_time = load_time
        self.P = P
        self.load_need = int(self.load_time/delta_t) #Hypothèse que le besoin en charge est inférieur au temps total.
        self.load_start = int(load_start/delta_t)


def load_table(voitures):

    L = np.zeros((n_ev,n_intervalles))
    c1 = voitures[0].load_start
    c2 = voitures[0].load_need
    v=0

    while v+1<len(voitures):

        for t in range(c1, c2):
            L[v][t] = 1
            voitures[v].load_need = voitures[v].load_need - 1
            c1+=1
        
        if c1 == n_intervalles:
            v+=1
        else:
            while c1 < n_intervalles:
                while v+1<len(voitures):
                    while voitures[v+1].load_need>0:

                        L[v+1][c1]=1
                        voitures[v+1].load_need = voitures[v+1].load_need - 1
                        c1+=1

                        if c1 == n_intervalles:
                            break

                    if c1 == n_intervalles and voitures[v+1].load_need == 0:
                        v+=1
                        break            
                    elif c1 == n_intervalles and voitures[v+1].load_need > 0:
                        break
                    else:
                        v+=1
                if v+1 == len(voitures):
                    break 
                    
        c1 = voitures[v].load_start
        c2 = voitures[v].load_need
        
    return L

for i in range(n_ev):
    voit.append(Voiture(random.randint(120,480), random.randint(0,120), 6))

voit.sort(key = lambda x: x.load_start)

for i in range(n_ev):
    for t in  range(voit[i].load_start, voit[i].load_need):
        table_naive[i][t]=1

table_charge_opti = load_table(voit)
print(table_charge_opti) #Need trier par l'attribut load_start

puissance_smart = np.sum(table_charge_opti,0) * p_ev
puissance_naive = np.sum(table_naive,0) * p_ev

active_load_ev_naif = np.zeros((24))
for i in range(17, len(active_load_ev_naif)):
    active_load_ev_naif[i] = puissance_naive[(i-17)*6]

active_load_ev_smart = np.zeros((24))
for i in range(17, len(active_load_ev_naif)):
    active_load_ev_smart[i] = puissance_smart[(i-17)*6]
