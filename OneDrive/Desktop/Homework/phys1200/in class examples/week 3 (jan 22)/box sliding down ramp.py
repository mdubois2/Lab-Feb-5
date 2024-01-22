# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:25:50 2024

@author: mdubo
"""
import numpy
#package necessary for using cosine
g = 9.8;
#defining gravity
print("Input the mass of the box that is sliding in kg");
m = float(input());
print("Input the coefficient of kinetic friction");
uk = float(input());
print("Input the angle that the ramp that the box is sliding on makes with the ground in radians");
angle = float(input());
#obtains necessary values to solve equation

friction = float((m*g)*numpy.cos(angle)*uk)
#solves for friction force

print(str(friction) + " N")
#prints friction force


