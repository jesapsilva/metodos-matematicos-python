# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:38:26 2019

@author: jesap
"""
#------------------------------------------------------------------------
#           LANÇAMENTO DE UM PROJÉTIL
#------------------------------------------------------------------------

from math import *
import numpy as np
import matplotlib.pyplot as plt

#dados do problema
d=7e-2
mass=0.15
g=9.81
dt=0.01
T=50
v=30
theta=50

def inicializa(v,theta,T,dt):
    #posicao inicial x(m/s)
    x0=0
    #vetor posicao x
    x=np.zeros((int(T/dt)+1,1),dtype='float')
    #adicionar x0 no vetor posicao x
    x[0]=x0
    #posicao inicial y(m/s)
    y0=0.4
    #vetor posicao y
    y=np.zeros((int(T/dt)+1,1),dtype='float')
    #adicionar y0 no vetor posicao y
    y[0]=y0

    #velocidade inicial x(m/s)
    vx0=v*cos(theta*pi/180)
    #vetor velocidade x
    vx=np.zeros((int(T/dt)+1,1),dtype='float')
    #adicionar vx0 no vetor velocidade x
    vx[0]=vx0
    #velocidade inicial y(m/s)
    vy0=v*sin(theta*pi/180)
    #vetor velocidade y
    vy=np.zeros((int(T/dt)+1,1),dtype='float')
    #adicionar vy0 no vetor velocidade y
    vy[0]=vy0
    return x,y,vx,vy

def mdf(x,y,vx,vy,b,n):
    for i in range(1,len(vx)):
        vii=sqrt(vx[i-1]**2+vy[i-1]**2)
        vx[i]=vx[i-1]*(1-dt*b*vii**n/mass)      #velocidade em x
        x[i]=x[i-1]+dt*vx[i]                    #posicao em x
        vy[i]=vy[i-1]*(1-dt*b*vii**n/mass)-g*dt #velocidade em y
        y[i]=y[i-1]+dt*vy[i]                    #posicao em y
        
        if y[i]<=0:
            y[i]=0
            vy[i]=-vy[i]

        if x[i]>=200:
            x=x[:i]
            y=y[:i]
            break
    return x,y

#------------------------------------------------------------------------

# solucao sem atrito
x,y,vx,vy=inicializa(v,theta,T,dt)
b=0
x1,y1=mdf(x,y,vx,vy,b,-inf)

# solucao com atrito linear
x,y,vx,vy=inicializa(v,theta,T,dt)
beta=0.055
b=beta*d
x2,y2=mdf(x,y,vx,vy,b,0)

# solucao com atrito quadratico#
x,y,vx,vy=inicializa(v,theta,T,dt)
gama=0.1
b=gama*(d**2)
x3,y3=mdf(x,y,vx,vy,b,1)

#------------------------------------------------------------------------

# Gráficos
plt.legend(loc="right", bbox_to_anchor=[0, 1],
           ncol=2, title="Legenda")

plt.title("Lançamento de um projetil\n" )
plt.plot(x1,y1,'',label='vacuo')
plt.plot(x2,y2,':',label='atrito linear')
plt.plot(x3,y3,'-.',label='atrito quadratico')
plt.legend(shadow=True, fancybox=True)

plt.xlabel('\nx [m]')
plt.ylabel('\ny [m]')
plt.savefig('./figs/Lançamento de um projétil.png')
plt.show()

