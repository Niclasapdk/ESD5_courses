import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency in Hz
T = 1.0    # Signal duration in seconds
N = 1024   # Number of DFT points (can experiment with different values)
f1 = 50    # Frequency of first tone in Hz
f2 = 120   # Frequency of second tone in Hz
amplitude1 = 1.0  # Amplitude of first tone
amplitude2 = 0.8  # Amplitude of second tone

# Generate time vector
t = np.arange(0, T, 1/fs)

# Generate two-tone sinusoidal signal
signal = amplitude1 * np.sin(2 * np.pi * f1 * t) + amplitude2 * np.sin(2 * np.pi * f2 * t)

# Apply window function (experiment with different windows, e.g., Hamming, Blackman)
window = np.hamming(len(signal))
windowed_signal = signal * window

# Compute DFT
dft = np.fft.fft(windowed_signal, n=N)
frequencies = np.fft.fftfreq(N, 1/fs)

# Take the magnitude of the DFT
magnitude = np.abs(dft)

# Plot the results
plt.figure(figsize=(12, 6))

# Original signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label="Original Signal")
plt.title("Two-Tone Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Windowed signal
plt.subplot(3, 1, 2)
plt.plot(t, windowed_signal, label="Windowed Signal")
plt.title("Windowed Signal (Hamming)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# DFT magnitude
plt.subplot(3, 1, 3)
plt.plot(frequencies[:N//2], magnitude[:N//2], label="DFT Magnitude")
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()

plt.tight_layout()
plt.show()
