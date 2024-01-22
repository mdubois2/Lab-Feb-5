# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:14:11 2024

@author: mdubo
"""

g = -9.8;
#defining our acceleration
print("Input your initial velocity in meters per second");
v = float(input());
#obtains the initial velocity
print(str((-v**2)/(2*g)) + ' meters');