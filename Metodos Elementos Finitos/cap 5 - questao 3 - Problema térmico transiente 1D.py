# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:20:43 2019

@author: jesap
"""
#---------------------------------------------------------------------------------
#    SOLUÇÃO DE PROBLEMA TÉRMICO TRANSIENTE 1D USANDO ELEMENTOS FINITOS
#---------------------------------------------------------------------------------

#           Equação na forma fraca: (M/dt + K )Tn+1 = (M/dt)Tn

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# dados do problema + condição de contorno
Ti = 0.0
Tf = 1.0

# dados da malha
ne = 20
npoints = ne + 1 
L = 1.0
h = L/ne

# dados simulação
dt = 1
nIter = 201
t = 0.0

# dados para as matrizes
alpha = 1.0  #acompanha matriz de rigidez/difusão
b = 1.0 #acompanha a matriz de massa
c = 0.0 #acompanha o vetor f[i]

#---------------------------------------------------------------------------------
# CRIAÇÃO DA MALHA
X = np.linspace(0,L,npoints)   # vetor posição dos elementos5

IEN = np.zeros((ne,2),dtype='int') # criação da matriz de posição dos elementos

for e in range(0,ne):
    IEN[e,0] = e
    IEN[e,1] = e+1
#---------------------------------------------------------------------------------    
# criação da matriz de rigidez e de massa
K = np.zeros((npoints,npoints),dtype='float')
M = np.zeros((npoints,npoints),dtype='float')
F = np.zeros((npoints,1),dtype='float')
Z = np.zeros((npoints,npoints),dtype='float')


T = np.zeros((npoints,1),dtype="float")

#condições de contorno
T[0] = Ti
T[npoints-1] = Tf

# Gráfico condição inicial
plt.plot(X,T,'o--') #vamos plotar o vetor de temperatura inicial 
plt.xlabel('x [mm]')
plt.ylabel('Temperatura [ºC]')
plt.title(' Problema térmico transiente 1D com EF\n')
plt.savefig('./figs3/resultado0' + str(0) + '.png')                                                       
plt.clf()

#---------------------------------------------------------------------------------
# preenchendo as matrizes
for e in range(0,ne):
    #comprimento do elemento
    h = X[IEN[e,1]] - X[IEN[e,0]] 
    
    # matrizes do elemento linear
    k = dt*(alpha/h) * np.array([[1,-1],
                                 [-1,1]],dtype='float')
    
    m = (b*h/6.0)* np.array([[2,1],
                             [1,2]],dtype='float')
    
    f = (c*h/2.0) * np.array([[1],
                              [1]],dtype='float')    
    
    for i in range(0,2):
        ii = IEN[e,i]
        
        # montagem ( assembly) do vetor do lado direito
        F[ii,0] = F[ii,0] + f[i,0]
        
        for j in range(0,2):
            jj = IEN[e,j]
            
            K[ii,jj] = K[ii,jj] + k[i,j]        
            M[ii,jj] = M[ii,jj] + m[i,j]  
            Z[ii,jj] = K[ii,jj] + M[ii,jj]

# imposição das condições de contorno nas matrizes
Z[0,0], Z[0,1] = 1.0, 0.0
Z[npoints-1,npoints-1], Z[npoints-1,npoints-2] = 1.0, 0.0

#---------------------------------------------------------------------------------
##   resolvendo o sistema ficar do tipo Tn+1 = inversa(Z)*b onde o vetor b 
##                       será o vetor b = M*Tn

for j in range(1,nIter):
    # vamos iniciar j com 1 pois já criei a primeira imagem la em cima e nao quero sobrepor
    b = np.dot(M,T)
    #resolvendo sistema linear para encontrar o novo vetor T    
    T = np.linalg.solve(Z,b)
    #avança no tempo
    t = t + dt
#---------------------------------------------------------------------------------    
#construção do grafico
    if j%10==0: 
        #plot do resultado em t = 0 + dt
        plt.plot(X,T,'o--')
#        plt.show()
        plt.xlabel('x [mm]')
        plt.ylabel('Temperatura [ºC]')
        plt.title(' Problema térmico transiente 1D com EF\n')
        plt.savefig('./figs3/resultado' + str(j) + '.png')                                                       
        plt.clf()

