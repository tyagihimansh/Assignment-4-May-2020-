# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:19:37 2020

@author: Himanshu Tyagi
"""
## Volume of a Hyper sphere
import numpy as np
def nSphereVolume(dim, itr):
    count_in_sphere = 0

    for count in range(itr):
        coordinate = np.random.uniform(-1.0, 1.0, dim)
        norm= coordinate * coordinate
        distance = np.sum(norm)
        if distance < 1.0:
            count_in_sphere += 1

    return (2.0**dim) * (count_in_sphere / itr)
print('Area of Circle=', nSphereVolume(2, 100000))
print('Volume of 10-D Hypersphere=', nSphereVolume(10, 100000))