# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:04:58 2020

@author: Himanshu Tyagi
"""
def prescription(p):
    if p<1:
        print('Not Sufficiently Random')
    elif p>1 and p<5:
        print('suspect')
    elif p>5 and p<10:
        print('almost Suspect')
    else:
        print('sufficiently Random')
import numpy as np
from scipy import stats
score = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #counts for  two dice
oc1 = np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]) ##observation 1
oc2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]) ##observation 2
print('total observation=', np.sum(oc1), np.sum(oc2))  ##on running the code got 144
Ys = np.array([4, 8, 12, 16, 20, 24, 20, 16, 12, 8, 4]) ##Statistical prediction
V1 = ((oc1 - Ys)**2)/Ys
V2 = ((oc2 - Ys)**2)/Ys
v1 = np.sum(V1); v2 = np.sum(V2)
p1= (1 - stats.chi2.cdf(v1, len(oc1) - 1))*100
p2= (1 - stats.chi2.cdf(v2, len(oc2) - 1))*100
print('P[V>v1]=', p1, 'P[V>v2]=', p2)
prescription(p1) ##for observation 1
prescription(p2) ##for observation 2