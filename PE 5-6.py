# DEU NAOE Design of Autonomous Navigation System
# Made by jlee@deu.ac.kr on 2021.04.07
# Program example 5-6
# 2D & 3D plot of Unit step response

import numpy as np
import os
import matplotlib.pyplot as plt
import control
from control.matlab import *

t = np.linspace(0, 10, 101)
zeta = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

yout_Total = [[0 for col in t]]

for n in range(len(zeta)):
    num = [1]
    den = [1, 2*zeta[n], 1]
    sys = tf(num, den)
    yout, t = step(sys, t)
    yout_Total.append(yout)

del yout_Total[0]
yout_Total = np.array(yout_Total)

# 2D plotting
plt.figure(1)
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.title("Plot of Unit-Step Response Curves with " r'$\omega_n$ = 1' "  \n and " r'$\zeta$ = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0')
plt.xlabel("Time (sec)")
plt.ylabel("Response")
for n in range(len(zeta)):
    plt.plot(t, yout_Total[n])

plt.text(4.1, 1.86, r'$\zeta$ = 0')
plt.text(3.5, 1.50, '0.2')
plt.text(3.5, 1.24, '0.4')
plt.text(3.5, 1.08, '0.6')
plt.text(3.5, 0.95, '0.8')
plt.text(3.5, 0.86, '1.0')
plt.savefig('5-22_1.png')

# 3D plotting
plt.figure(2)
ax = plt.axes(projection='3d')

y = np.linspace(0, 1, len(zeta))

t, y = np.meshgrid(t, y)
ax.plot_surface(t, y, yout_Total)
ax.azim = -140
ax.elv = 10
ax.set_title("Three-Dimensional Plot of Unit-Step Response Curves")
ax.set_xlabel("t (sec)")
ax.set_ylabel(r'$\zeta$')
ax.set_zlabel("Response")
plt.savefig('5-22_2.png')
plt.show()