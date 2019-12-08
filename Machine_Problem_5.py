# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:31:23 2019

@author: Wency
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt


n = np.linspace(0,199,200)
x1 = input("Please input function x(n): ")

def program5(x):
    y = np.zeros(200)
    for m in n:
        m = int(m)
        if m == 0:
            y[m] = -1.5*x[m] + 2*x[m+1] - 0.5*x[m+2]
    
        elif m > 0 and m <= 198:
            y[m] = 0.5*x[m+1] - 0.5*x[m-1]
     
        elif m == 199:
            y[m] = 1.5*x[m] - 2*x[m-1] + 0.5*x[m-2]
    
    plt.legend('x-axis','y-axis')
    plt.title("Graph of function")
    plt.plot(n,x,label ='x(n)', color= "magenta")
    plt.plot(n,y,label ='y(n)', color= "cyan")  
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
program5(eval(x1))

