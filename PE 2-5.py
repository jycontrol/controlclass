# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.03.07
# Program example 2-3


import os
import matplotlib.pyplot as plt  # MATLAB plotting functions
import control as ct
from control.matlab import *

A = [[0, 1], [25, -4]]
B = [[1 ,1], [0, 1]]
C = [[1, 0], [0, 1]]
D = [[0, 0], [0, 0]]


sys = ct.ss(A,B,C,D)
sys2 = ct.tf(sys)
print(sys2)
 