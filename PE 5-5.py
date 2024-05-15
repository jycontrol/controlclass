# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.04.05
# Program example 5-5
# Unit step response

import numpy as np
import os
import matplotlib.pyplot as plt
import control
from control.matlab import *

num = [25]
den = [1, 4, 25]
sys = tf(num,den)
T = np.linspace(0, 3, 101)
yout, T = step(sys,T)

plt.figure(1)
plt.plot(T, yout)
plt.title('Unit-Step Response of G(s) = 25/(s^2 + 4s +25)')
plt.ylabel('Amplitude')
plt.xlabel('Time (sec)')
plt.ylim([0, 1.4])
plt.xlim([0, 3.0])
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.savefig('5-20.png')
plt.show()
