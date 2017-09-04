#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:03:11 2017

@author: niklasinde
"""
import sys
import sympy as sm
import numpy as np
from numpy import *
import matplotlib as plt
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt




class spline():
    """ Class to calculate a spline"""
    def __init__(self,points):
#        if len(points) > deg-2:
#            raise IndexError("You dont have enough points to mach the desired polynomial degree.\n Add points or lower the degree.")
        self.p = points
#        self.k = deg
        self.x = sm.Symbol("x")
        self.loader()


    #### Loading functions ###
    """ functions that will load when a variable is called with this class"""

    def ref(self):
        """creates a list with values between the x values in points
        because sympy.Symbol("x") cant select a value and we need a x-value
        in the recurrence function"""
        xi =[]
        for i in range(len(self.p)-1):
            xi.append(self.p[i]+self.p[i+1]/2)
        return(xi)



    def rec(self,i,k,xi):
        """recurrence formula for b-spline"""
        
        
        if k == 0:
            if self.p[i-1]==self.p[i]:
                return(0)
            elif points[i-1] <= xi and xi < points[i]:
                return(1)
            else:
                return(0)
        elif k > 0:
            # This formula is taken from an older project dubble check that this is correct.
            u = ((self.x-self.p[i-1])/(self.p[i+k-1]-self.p[i-1]))*self.rec(i,k-1,xi)+((self.p[i+k]-self.x)/(self.p[i+k]-self.p[i]))*self.rec(i+1,k-1,xi)
            u = ((self.x-self.p[i-1])/(self.p[i+k-1]-self.p[i-1]))*self.rec(i,k-1,xi)+((self.p[i+k]-self.x)/(self.p[i+k]-self.p[i]))*self.rec(i+1,k-1,xi)
            return(u)

    def loader(self):

        ### We create the xi variable to keep track of what interval we are currently working on
        self.xi = self.ref()
        ### N is the basis functions
        self.N = [self.rec(i+1,3,self.xi[i]) for i in range(len(self.p)-4)]

    ##########################################################################3





    def basicplot(self):
        for i in range(len(self.N)):
            evalfunc = lambdify(self.x, self.N[i], modules=['numpy'])
            y = linspace(self.p[i+1],self.p[i+2]+0.11,50)
            plt.plot(y,evalfunc(y))
        plt.title("Plot of the basic functions for the splines")
        plt.show()




    ### Evaluation functions ###
    def hotareapoints(self,x):
        """ If x is between points p_i and p_{i+1} this function will return points p_{i-2} to p_{i"""
        ### First check if x is a valid value given the point. (note that x must be defined between p_2 and p_k-2)
        if self.p[2] > x or x > self.p[-2]:
            raise ValueError("X is not in the given interval")
        for i in range(len(self.p)-1):
            if self.p[i] < x and x < self.p[i+1]:
                return([j for j in range(i-2,i+2)]) # Check the index here, how many dots are needed!!


    def eval(self,x):
        if self.p[2] < x and x < self.p[-2]:
            raise ValueError("x must have a value between"+ self.p[2] +" and "+ self.p[-2])







points = [0,1/6,2/6,3/6,4/6,5/6,1]
a = spline(points)
a.basicplot()
"""
Från wiki

def deBoor(k, x, t, c, p):

#    Evaluates S(x).
#
#    Args
#    ----
#    k: index of knot interval that contains x
#    x: position
#    t: array of knot positions, needs to be padded as described above
#    c: array of control points
#    p: degree of B-spline

    d = [c[j + k - p] for j in range(0, p+1)]
    for r in range(1, p+1):
        for j in range(p, r-1, -1):
            alpha = (x - t[j+k-p]) / (t[j+1+k-r] - t[j+k-p])
            d[j] = (1.0 - alpha) * d[j-1] + alpha * d[j]
    return d[p]

"""
