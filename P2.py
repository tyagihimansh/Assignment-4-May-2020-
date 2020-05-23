# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:11:52 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
import time
t0 = time.time()
x=np.random.rand(10000)
t1=time.time()
print('Time=', t1-t0)
y=np.full(10000, 400)
plt.hist(x, bins=25, histtype='bar')
plt.plot(x,y,label='For Uniform PDF')
plt.xlabel(r'$\ x_i$')
plt.ylabel('Number in each bin')
plt.title('Density Histogram',fontsize=14)
plt.legend()
fig2=plt.show()
