# -*- coding: utf-8 -*-
"""
Created on Sun May 24 07:27:15 2020

@author: Himanshu Tyagi
"""
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sqrt(2/np.pi)*np.exp(-(x**2)/2)
def F(x):
    return 1.5*np.exp(-x)
x1 = np.arange(0, 10, 0.01)
x = np.random.rand(1000)
x = -np.log(x)
y = np.random.rand(1000)*F(x)
x_good = x[y < f(x)]; x_bad = x[y > f(x)]
y_good = y[y < f(x)]; y_bad = y[y > f(x)]
plt.plot(x_good, y_good,'.', label= 'Accepted Numbers', color=('green'))
plt.plot(x_bad, y_bad,'.', label= 'Rejected Numbers', color=('red'))
plt.plot(x1, F(x1), label= 'Envelope', color=('blue')) 
plt.plot(x1, f(x1), label= 'Desired PDF', color=('black'))
plt.legend()
plt.show()
plt.hist(x_good, bins= 10, density= True, label= 'Non-Uniform Deviate')
plt.plot(x1, f(x1), label= 'Desired PDF')
plt.legend()
plt.show()