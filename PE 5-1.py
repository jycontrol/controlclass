# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.04.05
# Program example 5-1
# MIMO system: 2 input, 2 output


import numpy as np
import os
import matplotlib.pyplot as plt  
import control
from control.matlab import *

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
plt.title("Step Response")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 1)
plt.plot(T, yout1[:,0], label='$y_1$')
plt.title('From U1')
plt.ylabel('To: Y1')
plt.ylim([-0.4, 0.6])
plt.grid(color='b', linestyle='--', linewidth=0.5)    
        
plt.subplot(2, 2, 3)
plt.plot(T, yout1[:,1], label='$y_2$')
plt.ylabel('To: Y2')
plt.ylim([0.0, 2.0])
plt.grid(color='b', linestyle='--', linewidth=0.5)   

plt.subplot(2, 2, 2)
plt.plot(T, yout2[:,0], label='$y_1$')
plt.title('From U2')
plt.ylim([-0.4, 0.6])
plt.grid(color='b', linestyle='--', linewidth=0.5)    
        
plt.subplot(2, 2, 4)
plt.plot(T, yout2[:,1], label='$y_2$')
plt.ylim([0.0, 2.0])
plt.grid(color='b', linestyle='--', linewidth=0.5)   

plt.savefig('5-18.png')
plt.show()