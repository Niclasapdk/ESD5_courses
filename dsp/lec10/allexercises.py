import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data from the provided text files
signal_without_noise = np.loadtxt('Signal_without_noise.txt')
signal_with_noise = np.loadtxt('Signal_with_noise(1).txt')

# Parameters
N = 1024  # FFT size
N_high_res = 10240  # High-resolution FFT size (10x)
fs = 8000  # Sampling frequency (8 kHz)

# Step 2: Perform FFT on the signal without noise (1024-point)
fft_signal = np.fft.fft(signal_without_noise, N)
freqs = np.fft.fftfreq(N, 1/fs)
magnitude_spectrum = np.abs(fft_signal)

# Plot the amplitude spectrum from DC to 8 kHz
plt.figure(figsize=(10, 6))
plt.plot(freqs[:N//2], magnitude_spectrum[:N//2])
plt.title('Amplitude Spectrum of the Damped Sinusoid (No Noise)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 8000)
plt.show()

# Step 3: Zoom in on the interval from DC to 200 Hz
plt.figure(figsize=(10, 6))
plt.plot(freqs[:N//2], magnitude_spectrum[:N//2])
plt.title('Zoomed Amplitude Spectrum (No Noise) - DC to 200 Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 200)
plt.show()

# Step 4: Perform high-resolution FFT (10240-point)
fft_signal_high_res = np.fft.fft(signal_without_noise, N_high_res)
freqs_high_res = np.fft.fftfreq(N_high_res, 1/fs)
magnitude_spectrum_high_res = np.abs(fft_signal_high_res)

# Zoom in on the interval from DC to 200 Hz (high resolution)
plt.figure(figsize=(10, 6))
plt.plot(freqs_high_res[:N_high_res//2], magnitude_spectrum_high_res[:N_high_res//2])
plt.title('Zoomed Amplitude Spectrum (No Noise, High-Resolution FFT) - DC to 200 Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 200)
plt.show()

# Step 5: Apply Hamming window to the original signal and perform FFT
hamming_window = np.hamming(len(signal_without_noise))
windowed_signal = signal_without_noise * hamming_window
fft_signal_hamming = np.fft.fft(windowed_signal, N_high_res)
magnitude_spectrum_hamming = np.abs(fft_signal_hamming)

# Zoom in on the interval from DC to 200 Hz with Hamming window
plt.figure(figsize=(10, 6))
plt.plot(freqs_high_res[:N_high_res//2], magnitude_spectrum_hamming[:N_high_res//2])
plt.title('Zoomed Amplitude Spectrum (Hamming Window) - DC to 200 Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 200)
plt.show()

# Step 6: Analyze the noisy signal
# Perform FFT on the noisy signal with a 1024-point FFT
fft_signal_noise = np.fft.fft(signal_with_noise, N)
magnitude_spectrum_noise = np.abs(fft_signal_noise)
magnitude_spectrum_db = 20 * np.log10(magnitude_spectrum_noise[:N//2])

# Plot the amplitude spectrum of the noisy signal
plt.figure(figsize=(10, 6))
plt.plot(freqs[:N//2], magnitude_spectrum_db)
plt.title('Amplitude Spectrum of the Noisy Signal (dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)
plt.xlim(0, 8000)
plt.show()

# Apply Hamming window to the noisy signal and perform FFT
windowed_signal_noise = signal_with_noise * hamming_window
fft_signal_noise_hamming = np.fft.fft(windowed_signal_noise, N)
magnitude_spectrum_noise_hamming = np.abs(fft_signal_noise_hamming)
magnitude_spectrum_noise_db_hamming = 20 * np.log10(magnitude_spectrum_noise_hamming[:N//2])

# Plot the amplitude spectrum of the windowed noisy signal
plt.figure(figsize=(10, 6))
plt.plot(freqs[:N//2], magnitude_spectrum_noise_db_hamming)
plt.title('Amplitude Spectrum of the Noisy Signal with Hamming Window (dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)
plt.xlim(0, 8000)
plt.show()

# Step 7: Calculate SNR
peak_frequency_index = np.argmax(magnitude_spectrum_noise_db_hamming[:N//2])
peak_amplitude_db = magnitude_spectrum_noise_db_hamming[peak_frequency_index]
noise_floor_db = np.mean(magnitude_spectrum_noise_db_hamming[100:N//2])  # Exclude peak region
snr_db = peak_amplitude_db - noise_floor_db

# Print results
print(f"Peak Amplitude at 80 Hz: {peak_amplitude_db:.2f} dB")
print(f"Average Noise Floor: {noise_floor_db:.2f} dB")
print(f"Signal-to-Noise Ratio (SNR): {snr_db:.2f} dB")
