# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:10:43 2019

@author: jesap
"""
#------------------------------------------------------------------------
#           VELOCIDADE TERMINAL DE UMA GOTA 
#------------------------------------------------------------------------

import matplotlib.pyplot as plt
import math 
import numpy as np

#dados da gota
D=0.0000015
ro=840.0
V=((math.pi)*(D**3))/6.0

#calculo de massa, beta, delta t e b que é o coeficiente de atrito
m=ro*V
beta=0.00016
b=beta*D

#dados do problema 
g = 10.0
v = 0.0
time = 0.0
dt = 0.0000001
nIter = 500

#------------------------------------------------------------------------
a = (dt*b)/m
for i in range(0,nIter):    
    v = v - (a*v) + (g*dt)
    time += dt
    plt.plot(time*100000,v,'bo')
    
vlim = -m*g/b
def solucaoanalitica(t):
    v = 0.0
    v = v*(np.exp(-b*t/m)) - vlim*(1-(np.exp(-b*t/m)))
    return v 

time2 = 0.0
for i in range(0,nIter):
    a = solucaoanalitica(time2)
    time2 += dt
    plt.plot(time2*100000,a,'c*')
    
#------------------------------------------------------------------------

# Gráficos    
plt.title("Velocidade  terminal de uma gota \n" )
plt.xlabel("\n Tempo [s] 10e-6")
plt.ylabel(" Velocidade [m/s] \n")
plt.savefig('./figs/Velocidade terminal de uma gota.png')
plt.show()   
    