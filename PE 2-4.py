# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.03.07
# Program example 2-3


import os
import matplotlib.pyplot as plt  # MATLAB plotting functions
import control
from control.matlab import *

num = [2, 1, 1, 2]
den = [1, 4, 5, 2]

sys = tf2ss(num,den)
print(sys)
