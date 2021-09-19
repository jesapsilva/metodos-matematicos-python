# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:38:26 2019

@author: jesap
"""
#------------------------------------------------------------------------
#           MOVIMENTO HORIZONTAL DE UM CARRINHO 
#------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# dados do problema
m=1.0
b=0.1

# dados da simulação
dt=0.1
time=0.0
nIter=1000

#------------------------------------------------------------------------
# velocidade inicial
v=10.0
for i in range(0,nIter):
    v = v - ((dt*b)/m)*v
    time += dt
    plt.plot(time, v,'co')
    if v < 1e-10:
        print('o ultimo valor de v é:',v)
        break

dt2 = 0.1
v01=10.00
for i in range(0,nIter):
    a = b*dt2/m
    y = v01*np.exp(-a)    
    plt.plot(dt2,y,'g*')
    dt2 = dt2 + 1.0
#------------------------------------------------------------------------

# Gráficos
plt.title("Massa mola sem dissipação\n" )
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade (m/s)")
plt.savefig('./figs/Movimento de um carrinho na horizontal.png')
plt.show()   
    
    
    