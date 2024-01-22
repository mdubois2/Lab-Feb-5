# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:00:02 2024

@author: mdubo
"""

print("Input the acceleration of the object in (m/s^2)");
a = float(input());
#obtains acceleration
print("Input the amount of time that the object accelerates in seconds");
t = float(input());
#obtains time
s = float((1/2)*a*t**2);
#calculates the distance the projectile travels, using float because of the 
#1/2
print(str(s) + ' meters');
#converts s back into a string because adding a float and a string in the
#print function causes an error