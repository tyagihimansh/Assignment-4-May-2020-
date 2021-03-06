# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:32:11 2020

@author: Himanshu Tyagi
"""
import numpy as np
import matplotlib.pyplot as plt
import time
def random_gen(n, a, c, X0, m=2**31):
    t0=time.time()
    rand=np.zeros(n)
    rand[0]=X0
    for i in range(1,n):
        rand[i]=((a*rand[i-1]+c)%m)
    t1 = time.time()
    m1= np.sort(rand)
    rand = rand/m1[len(rand)-1]
    x=np.arange(0,n,1)
    plt.plot(x,rand,'.')
    plt.xlabel(r'$\ i$')
    plt.ylabel('Values of numbers')
    plt.title('Number distribution',fontsize=14)
    fig=plt.show()
    plt.hist(rand, bins=25, histtype='bar', density= True)
    y=np.full(10000, 1)
    plt.plot(rand,y,label='For Uniform PDF')
    plt.xlabel(r'$\ x_i$')
    plt.ylabel('Number in each bin')
    plt.title('Density Histogram',fontsize=14)
    plt.legend()
    fig2=plt.show()
    return print(rand), fig, fig2, print('Time=', t1-t0)   


random_gen(10000, 645949, 5985254, 1)

#Numbers generated by Congruential random generator are distributed almost uniformly





    