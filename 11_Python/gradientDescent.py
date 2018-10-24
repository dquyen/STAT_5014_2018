""""
Name: Quyen Do
Assignment: 11_Python
File: gradientDescent.py
Summary: a gradient descent algorithm 
        to compute the roots of a function
"""


#Loading necessary libraries
import numpy as np 
from scipy.misc import derivative
import pandas as pd 
import matplotlib.pyplot as plt
import math

# Class to hold return objects for solve_using_newtons function

# Define function
def fun1(x):
    return pow(3,x) - math.sin(x) + math.cos(5*x)

# Create a class to return the result
# A future's work
'''
class gdSolution(object):
  def __init__(self, solution, plot, tolerance):
    self.solution = 0
    self.plot = None
    self.tolerance = 0


  def print(self):
    print("Estimated solution is " + self.solution)
    self.plot.show()
    # show graph
'''

def solve_using_Newtons(guess,FUN,tolerance):
    
    #Set up max iteration
    max_iteration = 1000
    iteration_index = 0

    #Find the value of FUN based on guess
    x_n = guess
    f_n = FUN(guess)
    df_n =  derivative(FUN,x_n, dx= 1e-6)

    #Set up lists to hold iteration data
    x_list = []
    y_list = []
    deriv_list = []
    
    #Iterations to find the best solution within given tolerance
    while abs(f_n) > tolerance and iteration_index <= max_iteration:
        x_list.append(x_n)
        y_list.append(f_n)
        deriv_list.append(df_n)

        #Generate new x to check for solution
        x_n = x_n - (f_n/df_n)
        f_n = FUN(x_n)
        df_n = derivative(FUN,x_n,dx= 1e-6)
        #update the iteration index
        iteration_index += 1
        
        if iteration_index > max_iteration:
            print ("Unable to converge")
            return None
        
    # Loop breaks when a solution within tolerance is found
    # Save the last iteration, which is also the final solution
    x_list.append(x_n)
    y_list.append(f_n)

    # Create plot showing iteration
   
    # Graphing the function
    x_seq = np.arange(min(x_list)-1,max(x_list)+1,0.1)
    y_seq = []
    for x in x_seq:
        y_seq.append(FUN(x))
    plt.plot(x_seq,y_seq,lw=2)

    # Add points of iteration
    plt.plot(x_list,y_list,"g^")

    # Add point of the final solution
    plt.plot(x_list[len(x_list)-1],y_list[len(y_list)-1],"bs")
    # Add the initial point
    plt.plot(x_list[0],y_list[0],"r^")
    
    # Add line segments of each iterations
    for i in np.arange(1,len(x_list)-1,1):
        plt.plot([x_list[i-1],x_list[i]],[y_list[i-1],0],lw=1)
        plt.plot([x_list[i],x_list[i]],[0,y_list[i]],'--')
    
    plt.show()
    return x_n

print("Gradient descent solution is ",solve_using_Newtons(2,fun1,10**(-7)))


