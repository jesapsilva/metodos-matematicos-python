# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:21:40 2019

@author: jesap
"""
#-------------------------------------------------------------------
#           SISTEMA MASSA MOLA SEM DISSIPAÇÃO
#-------------------------------------------------------------------

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
velo2=[]
temp2=[]
espaco2=[]
for i in range(0,npoints):
    v = v + (-dt*k*x)/m 
    x = x + dt*v
    velo2.append(v)
    espaco2.append(x)
    temp2.append(time)
    time = time +  dt  
    
plt.plot(espaco2,velo2,)
plt.title("Massa mola sem dissipacao\n" )
plt.xlabel("Espaço(s)")
plt.ylabel("Velocidade (m/s)")
plt.savefig('./figs/questao4espacofases.png')
plt.show()

#------------------------------------------------------------------------
velo=[]
temp=[]
espaco=[]
for i in range(0,400):
    v = v + (-dt*k*x)/m +(dt*g)
    x = x + (dt*v)
    velo.append(v)
    espaco.append(x)
    temp.append(time)
    time = time +  dt

plt.plot(temp,espaco)   
plt.title("Massa mola sem dissipação\n" )
plt.xlabel("Tempo [s]")
plt.ylabel("Velocidade [m/s]")    
plt.savefig('./figs/questao4.png')
plt.show()

#------------------------------------------------------------------------