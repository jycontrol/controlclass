# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.03.07
# Program example 2-1

import os
import matplotlib.pyplot as plt  # MATLAB plotting functions
import control
from control.matlab import *

num1 = [10]
den1 = [1,2,10]
sys1 = tf(num1, den1)

num2 = [5]
den2 = [1,5]
sys2 = tf(num2, den2)

sys3 = series(sys1, sys2)
print(sys3)

sys4 = parallel(sys1,sys2)
print(sys4)

sys5 = feedback(sys1,sys2)
print(sys5)