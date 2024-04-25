# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.03.07
# Program example 2-3


import os
import matplotlib.pyplot as plt  # MATLAB plotting functions
import control
from control.matlab import *

A = [[0, 1, 0],[0, 0, 1],[-5, -25, -5]]
B = [[0],[25],[-120]]
C = [1, 0 ,0]
D = [0]


sys = ss2tf(A,B,C,D)
print(sys)
# or sys_ss = ss(A,B,C,D)
#    sys2 = ss2tf(sys_ss)