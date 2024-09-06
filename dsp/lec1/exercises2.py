import numpy as np
import matplotlib.pyplot as plt

# Constants
RC = 1e-3  # R = 1 kOhm, C = 1 microFarad
fs = 8e3  # Sampling frequency 8 kHz
T = 1 / fs  # Sampling period

# Number of samples to calculate
n_samples = 150

# Impulse response h[n]
h = (T / RC) * np.exp(-np.arange(n_samples) * T / RC)

# Input signal x[n] (unit step function)
x = np.ones(n_samples)

# Output y[n] calculation using convolution
y = np.zeros(n_samples)
for n in range(n_samples):
    for k in range(n + 1):  # Convolution sum only up to current index n
        y[n] += h[k] * x[n - k]  # Apply the convolution sum formula

# Plotting the response
print(y)
plt.figure(figsize=(10, 6))
plt.stem(np.arange(n_samples), y, basefmt=" ")
plt.title('Output y[n] of the Digital Filter')
plt.xlabel('Sample n')
plt.ylabel('Output y[n]')
plt.grid(True)
plt.show()

