import numpy as np
import matplotlib.pyplot as plt


with open("Signal_with_noise.txt", "r") as f:
    signal_temp = f.read().split()
    signal_ms = [float(num) for num in signal_temp]
    

with open("Signal_without_noise.txt", "r") as f:
    signal_temp = f.read().split()
    signal_us = [float(num) for num in signal_temp]

#########   Input Values    #############
n_samples = len(signal_ms)
RC = 1e-3  # R = 1 kOhm, C = 1 microFarad
fs = 8e3  # Sampling frequency 8 kHz
T = 1 / fs  # Sampling period
#########################################



# Impulse response h[n]
h = (T / RC) * np.exp(-np.arange(n_samples) * T / RC)

y = np.zeros(n_samples)
for n in range(n_samples):
    y[n] += signal_ms[n]

z = np.zeros(n_samples)
for n in range(n_samples):
    z[n] += signal_us[n]

# Output y[n] calculation using convolution
s = np.zeros(n_samples)
for n in range(n_samples):
    for k in range(n + 1):  # Convolution sum only up to current index n
        s[n] += h[k] * signal_ms[n - k]  # Apply the convolution sum formula

#plot signals
plt.plot(y, label='Signal with noise')
plt.plot(z, label='Signal without noise')
plt.plot(s, label='Signal filtered')

# naming the x axis
plt.xlabel('Samples')
# naming the y axis
plt.ylabel('Sample value')
# giving a title to my graph
plt.title('Compare signals and filter')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()