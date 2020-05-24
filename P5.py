# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:01:19 2020

@author: Himanshu Tyagi

Box Mullar method 
"""
import numpy as np
import matplotlib.pyplot as plt
def y(x):
    return np.exp(-(x**2)/2)/np.sqrt(2*np.pi)
x = np.arange(-4,4,0.1)
y = y(x)
x1 = np.random.rand(10000)
x2 = np.random.rand(10000)
y1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
plt.subplot(221)
plt.hist(y1, bins=100, density=True)
plt.plot(x, y, label='Gaussian')
plt.title('y1')
plt.legend(prop={'size':8})
plt.subplot(222)
plt.hist(y2, bins=100, density = True)
plt.plot(x, y, label='Gaussian')
plt.legend(prop={'size':8})
plt.title('y2')
plt.show()