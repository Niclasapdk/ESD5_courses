import numpy as np
import matplotlib.pyplot as plt

# Define the frequency range for digital frequency ω
omega = np.linspace(0, np.pi, 1000)  # From 0 to π radians/sample

# Map ω to analog frequency Ω using the inverse bilinear transform
T = 10
Omega = (2 / T) * np.tan(omega / 2)

# For T = 2
T = 2
Omega = np.tan(omega / 2)

# Compute Analog Frequency Response H(jΩ)
s = 1j * Omega
H_s = 2 / ((s + 1) * (s + 3))
mag_H_s = np.abs(H_s)

# Compute Digital Frequency Response H(e^{jω})
z = np.exp(1j * omega)
H_z = 2 * (z + 1)**2 / ((21 * z - 19) * (23 * z - 17))
mag_H_z = np.abs(H_z)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(omega, mag_H_s, label='Analog Filter |H(jΩ)|')
plt.plot(omega, mag_H_z, label='Digital Filter |H(e^{jω})|', linestyle='--')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.title('Magnitude Response Comparison')
plt.legend()
plt.grid(True)
plt.show()
