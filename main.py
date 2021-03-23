import numpy as np

intervalle_temps = 480
delta_t = 10
n_intervalles = int(intervalle_temps/delta_t)
n_ev = 10

class Voiture:
    def __init__(self, load_time, P):
        self.load_time = load_time
        self.P = P
        self.load_need = int(self.load_time/delta_t) #Hypothèse que le besoin en charge est inférieur au temps total.

    def load():
        self.load_need-=1

def load_table(voitures):

    L = np.zeros((n_ev,n_intervalles))
    c1 = 0
    c2 = voitures[0].load_need
    v=0

    while v<len(voitures):

        for t in range(c1, c2):
            L[v][t] = 1
            voitures[v].load
            c1+=1
        
        reste = n_intervalles-c1

        while reste > 0 :
            while voitures[v+1].load_need>0 and v+1<len(voitures):
                    L[v+1][c1]=1
                    voitures[v+1].load
                    c1+=1

                    reste = n_intervalles-c1
            v+=1

        c1 = 0
        c2 = voitures[v].load_need()

    return L

voit = []
for i in range(10):
    voit.append(Voiture(120, 3))

print(load_table(voit))

print(voit[0].load_need)        

