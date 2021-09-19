# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:55:30 2019

@author: jesap
"""
#------------------------------------------------------------------------
#                       OSCILADOR VAN DER POL
#------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 
import math 
import time 

#------------------------------------------------------------------------
def plot_van(mi,vn,xn):
    # dados do problema
    time = 0.0
    dt = 0.05
    velo = [vn]
    tempo = [time]
    espaco = [xn]
    
    while time < 80.0:  
        x = xn + dt*vn 
        v = vn + ((dt*mi)*(1-(x**2))*vn) - dt*xn
        vn = v
        xn = x   
        velo.append(v)
        tempo.append(time)
        espaco.append(xn)
        time += dt
        
    plt.plot(tempo,velo,'c--')
    plt.title("Oscilador Van Der Pol com mi = " + str(mi) )
    plt.xlabel("Tempo(s)")
    plt.ylabel("Velocidade (m/s)")
    plt.savefig('./figs/Oscilador Van Der Pool com mi = ' + str(mi) +'.png')
    plt.show()
    return espaco,velo
#------------------------------------------------------------------------
#Trabalhando com a função + Gráficos
    
 #dados do problema
vn = 0.1
xn = 0.2
mi = 1.5   

espaco,velo = plot_van(mi,vn,xn)
plt.plot(espaco,velo,'c--')
plt.title("Espaço de fase - Oscilador Van Der Pol com mi = " + str(mi) )
plt.xlabel(" Espaço (m)")
plt.ylabel("Velocidade (m/s)")
plt.savefig('./figs/Espaço de fase - Oscilador Van Der Pol com mi = '  + str(mi)+ '.png')
plt.show()

#------------------------------------------------------------------------
