# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:59:54 2019

@author: jesap
"""
#------------------------------------------------------------------------
#                          MASSA MOLA AMORTECEDOR
#------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math
import time

#condições do problema
g = 9.81
m = 1.0
v = 10.0
x = 0.0

#dados da simulação
nIter = 1000
dt = 0.1
time = 0.0

#------------------------------------------------------------------------

#analise de beta e omega
#omega = float(input('Entre com o valor de omega: ' ))
#beta = float(input('\nEntre com o valor de beta: ' ))

omega = 0.5
beta = 0.50

tempo =[]
velo = []
espaco = []

for i in range(0,nIter):
    v = v + (dt)*((-2*beta*v) -((omega**2)*x))
    x = x + dt*v   
    espaco.append(x)
    velo.append(v) 
    time += dt 
    tempo.append(time)
#------------------------------------------------------------------------
    
# Gráfico
plt.plot(tempo,espaco,'c-')    
plt.title("Massa mola com dissipação beta = " + str(beta)  )
plt.xlabel("Espaço(m)")
plt.ylabel("Tempo (s)")
 
plt.savefig('./figs/Massa mola com dissipação beta = ' + str(beta)+ '.png')
plt.show()