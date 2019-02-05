import random
import math

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.backend_bases as base

Oxygen = {
    'q' : -0.834
}
Hydrogen = {
    'q' : 0.41
}
class Atom:
    def __init__(self, type):
        self.pos = []
        self.charge = type['q']
    def setpos(self, x, y, z):
        self.pos = [x, y, z]
    def getpos(self):
        return self.pos

class Molecule:
    def __init__(self):
        self.O = Atom(Oxygen)
        self.H1 = Atom(Hydrogen)
        self.H2 = Atom(Hydrogen)
    def setpos(self, x, y, z):
        self.O.setpos(x,y,z)
        phi_H1 = random.uniform(0,math.pi)
        phi_H2 = math.pi+phi_H1
        theta = 0.91210907 # 52.26 degrees in radians
        r0 = 0.9572
        flipx = random.choice([1,-1])
        flipy = random.choice([1,-1])
        flipz = random.choice([1,-1])
        self.H1.setpos(x+flipx*r0*math.sin(theta)*math.cos(phi_H1),
                       y + flipy*r0*math.sin(theta)*math.sin(phi_H1),
                       z + flipz*r0*math.cos(theta))
        self.H2.setpos(x + flipx * r0 * math.sin(theta) * math.cos(phi_H2),
                       y + flipy * r0 * math.sin(theta) * math.sin(phi_H2),
                       z + flipz * r0 * math.cos(theta))

    def getpos(self):
        return [self.O.getpos(), self.H1.getpos(), self.H2.getpos()]


nParticles = 216
boxlength = 20
colors = []
for i in range(nParticles):
    colors.append('red')
    colors.append('black')
    colors.append('black')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xs = []
ys = []
zs = []
molecule_list = []
perSide = int(math.ceil((nParticles) ** (1. / 3.)))
# Evenly distribute n particles throughout a 3D box with side length=boxlength
for i in range(1, perSide + 1):
    for j in range(1, perSide + 1):
        for k in range(1, perSide + 1):
            if len(molecule_list) < nParticles:
                m = Molecule()
                m.setpos((i*(boxlength / perSide) - 0.5), j*(boxlength / perSide) - 0.5, k*(boxlength / perSide) - 0.5)
                for elem in m.getpos():
                    xs.append(elem[0])
                    ys.append(elem[1])
                    zs.append(elem[2])
            molecule_list.append(m)

#ax1.scatter(xs, ys, zs, c=colors, s=100)
#print(molecule_list)
colors = []
sizes = []
for i in range(nParticles):
    colors.append("red")
    colors.append("black")
    colors.append("black")
    sizes.append(240)
    sizes.append(80)
    sizes.append(80)
ax1.scatter(xs, ys, zs, marker='o', linestyle='-', c=colors, s=sizes)
plt.show()
