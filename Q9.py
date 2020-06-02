#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:48:12 2020

@author: himanshu tyagi
"""
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	if (x<7 and x>3):
		return 1
	else:
		return 0
x=np.zeros(10000)
y=np.linspace(-10,10,10000)
pdf=np.zeros(len(y))
n = 10000
x[0]=5.0
for i in range(n - 1):
	pdf[i] = f(y[i])/4
	Y = x[i] + np.random.normal(loc=0, scale=2)
	rand = np.random.rand()
	if (f(Y)/f(x[i])>rand):
		x[i+1] = Y
	else:
		x[i+1] = x[i]
plt.plot(x, label='Markov Chain')
plt.xlabel('ith step')
plt.ylabel('Value')
plt.legend()
plt.show()
plt.hist(x, bins=15, density=True, label='PDF using MCMC')
plt.plot(y, pdf, color='red', label='Given PDF')
plt.xlabel('x')
plt.ylabel('Probability distribution')
plt.title('Density Histogram')
plt.legend()
plt.show()