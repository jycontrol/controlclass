# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.04.05
# Program example 5-2
# MIMO system: 2 input, 2 output


import numpy as np
import os
import matplotlib.pyplot as plt  
import control
from control.matlab import *

# Enter matrices A,B,C, and D
A = [[-1,-1],[6.5,0]]
B = [[1,1],[1,0]]
C = [[1,0],[0,1]]
D = [[0,0],[0,0]]

sys = ss(A,B,C,D)

# Step response for the system
T = np.linspace(0, 10, 101)
yout1, T = step(sys, input = 0)
yout2, T = step(sys, input = 1)

plt.figure(1)
plt.plot(T, yout1[:,0], label='$y_1$')
plt.plot(T, yout1[:,1], label='$y_1$')
plt.title('Step Response Plots: Input = u1 (u2 = 0)')
plt.xlabel("Time (sec)")
plt.ylabel('Amplitude')
plt.text(3.4, -0.06, 'Y1')
plt.text(3.4, 1.4, 'Y2')
plt.ylim([-0.4, 2])
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.savefig('5-19_1.png')

plt.figure(2)
plt.plot(T, yout2[:,0], label='$y_2$')
plt.plot(T, yout2[:,1], label='$y_2$')
plt.title('Step Response Plots: Input = u2 (u1 = 0)')
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.text(3.0, 0.14, 'Y1')
plt.text(2.8, 1.1, 'Y2')
plt.ylim([-0.4, 1.6])
plt.grid(color='b', linestyle='--', linewidth=0.5)

plt.savefig('5-19_2.png')
plt.show()