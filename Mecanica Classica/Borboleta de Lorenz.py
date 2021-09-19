# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:27:23 2019

@author: jesap
"""
#                          BORBOLETA DE LORENZ

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

#parametros do problema
r = 28.0 
b = 8.0/3.0 
s = 10.0

# vetores com os valores de z calculados + condição inicial
xs = np.empty((npoints + 1,))
ys = np.empty((npoints + 1,))
zs = np.empty((npoints + 1,))

#condições iniciais
v = 0.0
xs[0], ys[0], zs[0] = (0., 1., 1.05)

#parametros da simulação
npoints = 10000
dt =0.01

#função Lorentz
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x) + x
    y_dot = r*x - y - x*z + y
    z_dot = x*y - b*z + z
    return x_dot, y_dot, z_dot

for i in range(npoints):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Grafico    
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Borboleta de Lorenz")
plt.savefig('./figs/Grafico10_BorboletaLorenz.png')
plt.show()

    