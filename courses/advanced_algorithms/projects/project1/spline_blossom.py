#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:03:11 2017

@author: niklasinde
"""
import sys

import numpy as np
from numpy import *
import matplotlib as plt
from sympy.utilities.lambdify import lambdify
import sympy as sm
import matplotlib.pyplot as plt
import sympy
import scipy



class spline():
    """ Class to calculate a spline"""
    def __init__(self,points,coeff = None):
#        if len(points) > deg-2:
#            raise IndexError("You dont have enough points to mach the desired polynomial degree.\n Add points or lower the degree.")
        
        self.k = 3
        self.points = points
        if not type(coeff) == np.ndarray:
            self.coeff = [1 for i in range(len(points)-self.k-1)]
        else:
            self.coeff = coeff
#        self.k = deg
        self.x = sm.Symbol("x")
        self.loader()

    

    #### Loading functions ###
    """ functions that will load when a variable is called with this class"""

    def ref(self,p):
        """creates a list with values between the x values in points
        because sympy.Symbol("x") cant select a value and we need a x-value
        in the recurrence function"""
#        p = self.points
        xi =[]
        for i in range(len(p)-1):
            xi.append(p[i]+(p[i+1]-p[i])/2)
        self.e =[(p[i]+p[i+1]+p[i+2])/2 for i in range(len(p)-self.k)]
        self.xi = xi
        return(xi)



    def rec(self,p,i,k,xi):
        """recurrence formula for b-spline"""
        # note that p the p heres are local
        if k == 1:
            if p[i] == p[i+1]:
                return(0)
                
            if  p[i] < xi and xi <= p[i+1]:
                return(1)
            
            else:
                return(0)
        else:
            def div(lhs, rhs):
                if rhs == 0:
                    return 0 
                else:
                    return(lhs / rhs)
            u =  div((self.x-p[i]),(p[i+k-1]-p[i]))*self.rec(p,i,k-1,xi)+div((p[i+k]-self.x),(p[i+k]-p[i+1]))*self.rec(p,i+1,k-1,xi)
            return(u)

            
    def basicfunction(self):
        n1 = []
        for i in range(len(self.points)-self.k-1):
            n2=[]
            p = self.points[i:i+self.k+2]
            xi = self.ref(p)
            for j in range(self.k+1):
                n2.append(self.rec(p,0,self.k+1,xi[j]))
            n1.append(n2) 
        self.N = n1
#        print(self.N)
    
    def loader(self):
        ### loading function ###
        ### Call this if the points are updated ###
        self.basicfunction()
        
    
        
    

    ##########################################################################3

    def basicplot(self):
        """ Plots all the basis functions """

        for i in range(len(self.N)):
            for j in range(len(self.N[i])):
                if self.N[i][j]!= 0:
                    evalfunc = lambdify(self.x, self.N[i][j], modules=['numpy'])
                    y = linspace(self.points[i+j],self.points[i+j+1],50)
#                    print(type(y))
                    plt.plot(y,evalfunc(y))
        plt.ylim(0,1.2)
        plt.xlim(self.points[0],self.points[-1])
        plt.title("Plot of the basic functions for the splines")
        plt.show()
    
    def evalfull(self,X):
        p = self.points
#        print(p,"PPPPPPPP",x,"x")
#        if (p[self.k] > x).all() and (x > p[-self.k]).all():
#            print("X is not in the correct interval")
        y = []
        print(len(self.coeff),len(self.N),"do the matching match")
        for i in range(len(X)):
            hot_interval = self.hotinterval(X[i])
            func_val = 0
            g = 0 
            for j in range(hot_interval-self.k-1,hot_interval):
                evalfunc = lambdify(self.x, self.N[j+1][self.k-g], modules=['numpy'])
                func_val += self.coeff[j+1]*evalfunc(X[i])
                g+=1
            y.append(func_val)
        return(y)
            
    def evalbasis(self,x,i):
        p = self.points
        func_val=0
        hot_interval = self.hotinterval(x)
        if p[hot_interval] < x and x <= p[hot_interval+self.k+1]:
            return(0.)
#        if xi is in the function value return 0
        for j in self.N[i]:
            evalfunc = lambdify(self.x, j, modules=['numpy'])
            func_val += self.coeff[i]*evalfunc(x)
        return(func_val)    
        
        
        
    def hotinterval(self, x):
        p = self.points
        for i in range(len(p)):
            if p[i] <= x and x <= p[i+1]:
                return(i)
        
        raise ValueError("x is not in the interval")
        
        
        
class matrixequation():
    def __init__(self,xy,points):
        self.xy = xy
        self.p = points
        self.N = spline(points)

        self.xyvec = self.xyvector() 
        self.e = self.elist()
        self.A = self.Avector()
#        self.z = self.solver()
        
    def Avector(self):
        """creats a square tridiagonal matrix of size n"""
        n = len(self.N.N)
        A = np.zeros((n,n))
        for col in range(n):
            for row in range(n):
                A[row][col] = self.N.evalbasis(self.e[col],row)
        return(A)
    
    def elist(self):
        l = []
        p = self.p
        for i in range(len(self.N.N)):
            l.append((p[i]+p[i+1]+p[i+2])/3)
        return(l)
        
    def xyvector(self):
        """ When i write xy its because its the same function for x and y"""
        xy = np.array(self.xy)
        xy.reshape(len(self.xy),1)
        return(xy)
        
    def solver(self):
        print(self.A,self.xy)
        z = scipy.linalg.solve(self.A,self.xy)
        self.coeff = z
        
        print(self.coeff)
        return(z)
        

class interpolation():
    def __init__(self,points,x,y):
        
        self.xcoeff = matrixequation(x,points)
        self.ycoeff = matrixequation(x,points)
        
        self.splinex = spline(points,xcoeff.coeff)
        self.spliney = spline(points,ycoeff.coeff)
        
        
    def x(self,x):
        return(self.splinex.evalfull(x))
    def y(self,y):
        
        return(self.spliney.evalfull(y))
    
    
    
    
        
        
        
        




points = [0,0,0,1,2,3,4,5,6,7,7,7]
x = [1,2,3,4,5,1,4,4]
y = [1,2,2,10,6,2,4,4]
a = spline(points)
#d = d_iterative(points, 4, coeffs,a.xi)

#interpol= interpolation(points,x,y)


a = matrixequation(x,points).A
b = matrixequation(y,points).A
u = linspace(1,6,40)
#ux = interpol.x(u)
#uy = interpol.y(u)
plt.scatter(x,y)
plt.plot(ux,uy)
print(ux,uy)
#print(len(x),len(y))
#a.basicplot()
#plt.plot(x,y)

#a = interpolate(x,y,)
#print(a.N)