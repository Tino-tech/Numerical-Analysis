# -*- coding: utf-8 -*-
"""
@Name: Tinotenda Mhlanga
@Copyright: University of Nicosia 
@Project: Bisection Method

"""
from math import *

x1 = 0.1
x2 = pi
y1 = x1**2 - sin(x1)
y2 = x2**2 - sin(x2)

# Check for the sign difference between y-values
# If the signs are not opposite, stop

if y1*y2 > 0:
    print('Error: Root Not Found Within Given Interval')
    exit
    
for i in range(1, 101):
    # Calculate the value of x in the half of the interval
    x_half = (x1 + x2) / 2
    y_half = x_half**2 - sin(x_half)
    
    # Check for the sign difference between the y-values first half interval
    y1 = x1**2 - sin(x1)
    if abs(y1) < 1.0E-8:
        break
    elif y1 * y_half < 0: #If the root is in the first interval
        x2 = x_half
    else:
        x1 = x_half
        
print(f'Root: {round(x1, 2)}')
print(f'Number of bisections: {i}')

        
