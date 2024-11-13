import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def plot_filter_response(N, H, fs=8000):
    """
    Calculate filter coefficients and plot the frequency response of an FIR filter.

    Parameters:
    - N (int): Filter length.
    - H (array-like): Frequency response samples (should be of length (N + 1) // 2).
    - fs (int, optional): Sampling frequency in Hz. Default is 8000 Hz.
    """
    # Ensure H has the correct length
    expected_length = (N + 1) // 2
    if len(H) != expected_length:
        raise ValueError(f"Length of H should be {(N + 1) // 2}, but got {len(H)}.")

    # Calculate alpha
    alpha = (N - 1) / 2

    # Calculate the filter coefficients h(n)
    h = np.zeros(N)
    for n in range(N):
        sum_term = 0
        for k in range(1, (N - 1) // 2 + 1):
            sum_term += 2 * H[k] * np.cos(2 * np.pi * k * (n - alpha) / N)
        h[n] = (1 / N) * (sum_term + H[0])  # Include H[0] term

    # Display the filter coefficients
    print('Computed filter coefficients (h):')
    print(h)

    # Frequency response of the filter
    w, H_response = freqz(h, worN=1024, fs=fs)

    # Plot the frequency response
    fig = plt.figure(figsize=(10, 6))
    plt.plot(w, 20 * np.log10(abs(H_response)), linewidth=1.4)
    plt.title('Frequency Response of the FIR Filter', fontsize=18)
    plt.xlabel('Frequency (Hz)', fontsize=16)
    plt.ylabel('Magnitude (dB)', fontsize=16)
    plt.grid(True)
    plt.plot([750, 1000, 1500], [-1, -3, -10], 'ro', markerfacecolor='r')
    plt.legend(['Frequency Response', 'Target Points'], fontsize=14)

    # Add annotations
    # Prepare annotation text based on H values
    annotation_lines = [f'N = {N}']
    # If specific H values are provided, include them in annotations
    for i, h_value in enumerate(H[2:], start=2):
        annotation_lines.append(f'T_{i} = {h_value:.8f}')

    str_text = '\n'.join(annotation_lines)
    plt.annotate(str_text, xy=(0.65, 0.15), xycoords='axes fraction', fontsize=14,
                 bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=1))

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    return fig

fig = plot_filter_response(15, np.asarray([1, 1, 0.65951526, 0.17360713, 0.01000977, 0, 0, 0, 0]))
fig = plot_filter_response(15, np.asarray([1, 1, 0.65951526, 0.17360713, 0.01000977, 0, 0, 0, 0]))
