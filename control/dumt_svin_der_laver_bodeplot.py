import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the symbolic variable 's'
s = sp.symbols('s')

#########################################################################
# Define the transfer function H(s) = 10 / [(s + 1)^2 * (s + 10)]
numerator = [0.1]  # Coefficient of the numerator

# Define the denominator (s+1)^2 * (s+10)
denom = (s + 0.1) * (s + 10)*s
#########################################################################

# Expand the denominator
expanded_denom = sp.expand(denom)

# Display the expanded form
print(f"Expanded Denominator: {expanded_denom}")

denom_coeffs = sp.Poly(expanded_denom, s).all_coeffs()
denom_coeffs = [float(coeff) for coeff in denom_coeffs]  # Convert to float

# Output the coefficients without 's'
print(f"Denominator Coefficients (without 's'): {denom_coeffs}")

# Create the transfer function
system = signal.TransferFunction(numerator, denom_coeffs)

# Define the frequency range (logarithmically spaced) up to 100 rad/s
frequencies = np.logspace(-3, 3, 1000)  # From 0.01 rad/s to 100 rad/s

# Compute Bode plot data
w, magnitude, phase = signal.bode(system, frequencies)

# Plotting the Bode magnitude plot
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude)  # Bode magnitude plot
plt.title('Bode Plot')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# Plotting the Bode phase plot
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)  # Bode phase plot
plt.ylabel('Phase (degrees)')
plt.xlabel('Frequency (rad/s)')
plt.grid(True)

plt.show()
