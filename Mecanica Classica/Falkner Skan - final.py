# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:38:26 2019

@author: jesap
"""

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

#------------------------------------------------------------------------
#                           FALKNER SKAN
#------------------------------------------------------------------------ 

	
def num_plot(num_list,n):
    size = len(num_list)
    return_list = []
    for i in range(0,size,int(size/n)):
        return_list.append(num_list[i])
    return return_list
	
def main():
	
    global time
	
    f3_0 = [0.005218,0.4696,1.232588,1.687218]
    n_lim = [6.2,5,8.4,4.73]
    dn = [0.001,0.001,0.0001,0.00001]
    beta = [-0.1988,0,1,2]
    color = ["k","b","r","y"]
    time1 = time.time()
    for i in range(0,4):
        F1 = [0,]
        F2 = [0,]
        F3 = [f3_0[i],]
        N = [0,]
        n = 0
        while n < n_lim[i]:
            F1.append(dn[i]*F2[-1] + F1[-1])
            F2.append(dn[i]*F3[-1] + F2[-1])
            k1 = dn[i]*(-F1[-1]*F3[-1] - beta[i]*(1 - F2[-1]**2))
            k2 = dn[i]*(-F1[-1]*(F3[-1] + k1/2) - beta[i]*(1 - F2[-1]**2))
            F3.append(F3[-1] + (k1 + k2)/2)
            n += dn[i]
            N.append(n)
        plt.xlim([0,5])
        plt.ylim([0,1.1])
        string = color[i]+".-"
        plt.plot(num_plot(N,50),num_plot(F2,50),string,label = 'B = '+str(beta[i]),linewidth = 0.5)
        plt.legend(loc = 'best')
    time2 = time.time()
    print("Tempo decorrido: ",1000*(time2 - time1))

    
    plt.ylabel("f2")
    plt.xlabel("N")
    plt.show()

if __name__ == "__main__":
    main()
