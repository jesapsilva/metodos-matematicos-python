# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:21:40 2019

@author: jesap
"""
#------------------------------------------------------------------------
#           SISTEMA MASSA MOLA VERTICAL
#------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math
import time

# dados do problema
m =0.15
k = 0.1
g = 9.81
v = 10.0
x = 0.0

# dados da simulação
npoints = 4000
time = 0.0
dt = 0.1

#------------------------------------------------------------------------
for i in range(0,npoints):
    v = v + (-dt*k*x)/m + dt*g
    x = x + dt*v
    time = time + dt
    plt.plot(x,v,'co')
    plt.title("Massa mola vertical\n" )
    plt.xlabel("Espaço(s)")
    plt.ylabel("Velocidade (m/s)")
    
plt.savefig('./figs/Sistema mola vertical_espaço de fases.png')
plt.show()

#------------------------------------------------------------------------

for i in range(0,400):
    v = v + (-dt*k*x)/m +(dt*g)
    x = x + (dt*v)
    time = time +  dt
    plt.plot(time,v,'co')
    plt.title("Massa mola sem dissipação\n" )
    plt.xlabel("Tempo [s]")
    plt.ylabel("Velocidade [m/s]")

plt.savefig('./figs/Massa mola vertical_velocidade.png')
plt.show()

#------------------------------------------------------------------------