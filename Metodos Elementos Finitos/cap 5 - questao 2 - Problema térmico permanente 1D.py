# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:20:43 2019

@author: jesap
"""
#---------------------------------------------------------------------------------
#           TÉRMICO PERMANENTE 1D COM ELEMENTOS FINITOS
#---------------------------------------------------------------------------------

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# RESOLUÇÃO ELEMENTOS FINITOS 1D 

# MATRIZ K(elemento) = alfa/h(elemento)*[[1,-1],
#                                       [-1,1]]


#              condição de contorno
Ti=0.0
Tf=1.0

#           parametros geométricos
L = 1.0
ne = 5
npoints = ne - 1     #numero de elementos

#           parametros da simulação
alfa = 1.0
h = 1.0/ne
#---------------------------------------------------------------------------------
##   criando as matrizes do sistema linear Ax=b

#               vetor b 
b = np.zeros((npoints,1), dtype = 'float')  #   impondo as condições de contorno na matriz K 
                                            #   devido a isso b[1] = b[1] -(alfa/h)*Ti
                                            #   com isso b[npoints-1] = b[npoints-1] -(alfa/h)*Tf                                           
b[1] = -(alfa/h)*Ti
b[npoints-2] = -(alfa/h)*Tf
b[npoints-1]= 1.0

#           vetor posição dos n pontos
X =np.linspace(0,L,npoints)

#           criação da matriz de Rigidez
K = np.zeros((npoints,npoints), dtype='float' )  

#---------------------------------------------------------------------------------
# preenchendo as matrizes
for i in range(1,npoints-1):
    K[i,i] = -2*alfa/h 

for i in range(1,npoints-2):
    K[i,i+1] = alfa/h

for i in range(2,npoints-1):
    K[i,i-1] = alfa/h

#condições de contorno
K[0,0] = 1.0
K[npoints-1,npoints-1] = 1.0
#print('MATRIZ DE RIGIDEZ \n:', K)
#---------------------------------------------------------------------------------
#           resolvendo o sistema linear 
A = inv(K)
temps = np.dot(A,b)

#print('o vetor que mostra a variação da temperatura ao longo da barra é:\n',temps)
#---------------------------------------------------------------------------------

# Gráficos
for i in temps:
    plt.plot(X,temps,'o--')
       
plt.title("Problema 1D com elementos finitos \n" )
plt.xlabel("\n x [m]")
plt.ylabel("Temperatura [ºC] \n")
plt.savefig('./figs2/Grafico2-1Delementosfinitos.png')
plt.show()