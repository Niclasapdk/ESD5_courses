#import sympy as sp
import numpy as np
import math 
import matplotlib.pyplot as plt
#from scipy import signal
import control as ct
import control.matlab as m

s = ct.TransferFunction.s

#system
G = 10/((s+1)*(s+2)*s) 


#lead_controller
K = 25
center = 3
alpha = 10

a = center/alpha
b = center * alpha
D_lead = K*(s+a)/(s+b) 


d = 0.0001
c = 20*d
D_lag = (s+c)/(s+d)

#ct.bode_plot(G, display_margins=True, dB=True, grid=True, omega=np.logspace(-3, 2, 1000), label="G")
#ct.bode_plot(D_lead, display_margins=True, dB=True, grid=True, omega=np.logspace(-3, 2, 1000), label="D_lead")
#ct.bode_plot(D_lag, display_margins=True, dB=True, grid=True, omega=np.logspace(-3, 2, 1000), label="D_lag")
#ct.bode_plot(G*D_lead, display_margins=True, dB=True, grid=True, omega=np.logspace(-3, 2, 1000), label="G*D_lead")
#ct.bode_plot(G*D_lead*D_lag, display_margins=True, dB=True, grid=True, omega=np.logspace(-3, 2, 1000), label="G*D_lead*D_lag")

m.step(G*D_lead)
m.step(G*D_lead*D_lag)

plt.show()