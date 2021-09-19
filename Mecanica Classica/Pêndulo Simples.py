# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:51:57 2019

@author: jesap
"""
#------------------------------------------------------------------------
#                          PÊNDULO AMORTECIDO
#------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# dados do proble
m = 1.0
g = 9.81
dt = 0.1
l = 1.0

# dados da simualação
time = 0.0
v = 0.0
teta0 = 10*math.pi/180.0
teta = 10

#------------------------------------------------------------------------
matrizteta=[]
matriztempo=[]
matrizvelo=[]

for i in range(0,500):
    teta = teta + dt*v
    p = teta*math.pi/180.0
    v = v - (dt*g/l)*(np.sin(p))
    time += dt
    matrizteta.append(teta)
    matriztempo.append(time)
    matrizvelo.append(v)

#------------------------------------------------------------------------

# Gráficos    
plt.plot(matriztempo,matrizteta,'c-')
plt.title("Pêndulo Simples" )
plt.xlabel("Tempo(s)")
plt.ylabel("Teta (rad)")
plt.savefig('./figs/Pendulo simples.png')
plt.show()
    

plt.plot(matrizteta,matrizvelo,'c-')
plt.title("Pêndulo Simples" )
plt.xlabel("teta(rad)")
plt.ylabel("velocidade (rad/s)")
plt.savefig('./figs/Pendulo simples espacofase.png')
plt.show()
#------------------------------------------------------------------------