"""Implemented by Federico Zocco
    Last update: 13 September 2023

Numerical simulation of the vision-based system
detailed in [1] for resources mapping and quantification.


References:
[1] Zocco, F. and Rahimifard, S., 2023. Visual Material 
    Characteristics Learning for Circular Healthcare. 
    https://arxiv.org/abs/2309.04763
[2] Zocco, F., McLoone, S. and Smyth, B., 2022. Material 
    measurement units for a circular economy: Foundations 
    through a review. Sustainable Production and Consumption, 
    32, pp.833-850.      
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation settings:
t_final = 140 # seconds

T_p11 = 60 # unit 1, class 1 
T_p12 = 70 # unit 1, class 2
T_p21 = 80 # unit 2, class 1
T_p22 = 90 # unit 2, class 2

T_d11 = 80 # unit 1, class 1
T_d12 = 80 # unit 1, class 2
T_d21 = 80 # unit 2, class 1
T_d22 = 80 # unit 2, class 2

m1 = np.array([[1], [2], [3]]) # masses in class 1 (psi = 3)
m2 = np.array([[1], [2], [3]]) # masses in class 2 (psi = 3)

########################################
t = np.arange(0, t_final, 1)
startTime_11 = T_p11 - T_d11/2 # when the detection of class 1 begins in unit 1
startTime_12 = T_p12 - T_d12/2 # when the detection of class 2 begins in unit 1
startTime_21 = T_p21 - T_d21/2 # when the detection of class 1 begins in unit 2
startTime_22 = T_p22 - T_d22/2 # when the detection of class 2 begins in unit 2

# Masses detected by each unit:
xi_11 = np.where(abs((t - T_p11)/T_d11) < 0.5, 1, 0) 
xi_12 = np.where(abs((t - T_p12)/T_d12) < 0.5, 1, 0) 
xi_21 = np.where(abs((t - T_p21)/T_d21) < 0.5, 1, 0)
xi_22 = np.where(abs((t - T_p22)/T_d22) < 0.5, 1, 0)

m_1 = xi_11*m1 + xi_12*m2 # masses detected by unit 1; it is a function of time
m_2 = xi_21*m1 + xi_22*m2 # masses detected by unit 2; it is a function of time


# Plots:
fig = plt.figure(figsize=(10, 10))
plt.plot(t, m_1[0] + m_2[0], 'r-', linewidth=6)
plt.grid()
plt.xlabel(r"Time, $t$ (s)", fontsize=35) 
plt.ylabel(r"$\tau_1$ (kg)", fontsize=35) 
plt.xticks(fontsize=35)
plt.yticks(range(0, 14, 2), fontsize=35) 

fig = plt.figure(figsize=(10, 10))
plt.plot(t, m_1[1] + m_2[1], 'b-', linewidth=6)
plt.grid()
plt.xlabel(r"Time, $t$ (s)", fontsize=35)
plt.ylabel(r"$\tau_2$ (kg)", fontsize=35) 
plt.xticks(fontsize=35)
plt.yticks(range(0, 14, 2), fontsize=35) 

fig = plt.figure(figsize=(10, 10))
plt.plot(t, m_1[2] + m_2[2], 'k-', linewidth=6)
plt.grid()
plt.xlabel(r"Time, $t$ (s)", fontsize=35)
plt.ylabel(r"$\tau_3$ (kg)", fontsize=35) 
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)   