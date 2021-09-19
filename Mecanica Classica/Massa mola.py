# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:21:40 2019

@author: jesap
"""
#------------------------------------------------------------------------
#           SISTEMA MASSA MOLA SEM DISSIPAÇÃO
#------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 
import math 
import time 

#------------------------------------------------------------------------
# dados do problema
mi = 0.1
npoints = 65
dt = 20
xn = 0.45
time = 0.0
#------------------------------------------------------------------------

tempo = []
espaco = []

for i in range(0,npoints):
    x = mi*xn - mi*xn*xn
    xn = x
    time += dt
    espaco.append(x)
    tempo.append(time)
    
#------------------------------------------------------------------------

# Gráficos    
plt.plot(tempo,espaco,'-o')
plt.title("Sistema Massa Mola sem dissipação" )
plt.xlabel("\n Tempo [s]")
plt.ylabel("Velocidade [m/s] \n")
plt.show()


plt.plot(x,v,'co') 
plt.title("Sistema Massa Mola sem dissipação - Espaço de fases" )
plt.xlabel("\n Espaço [m]") 
plt.ylabel("Velocidade [m/s] \n")  
plt.savefig('./figs/Massa mola sem dissipação_espaço de fases.png')
plt.show()