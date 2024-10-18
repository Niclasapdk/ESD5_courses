from scipy.special import iv
import matplotlib.pyplot as plt
import numpy as np

def bessel_approx(x):
    return iv(0, x)

def kaiser(M, beta):
    assert M%2==0, "M is even"
    alpha = M//2
    n = np.arange(0, M+1)
    arg = beta * np.sqrt(1-pow((n-alpha)/alpha, 2))
    return bessel_approx(arg) / bessel_approx(beta)

def plot_timedomain(response):
    plt.figure()
    plt.plot(response)
    plt.title("Kaiser window")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")

def plot_fft(response):
    fresp = np.fft.fft(response)
    aresp_db = 20*np.log10(np.abs(np.fft.fftshift(fresp)))
    bins = np.fft.fftshift(np.fft.fftfreq(len(response))) * 2 * np.pi
    plt.figure()
    plt.plot(bins, aresp_db)
    plt.title("Kaiser window")
    plt.xlabel("Radian frequency (omega)")
    plt.ylabel("Amplitude (dB)")

win = kaiser(100, 1)
plot_timedomain(win)
plot_fft(win)
#plot_timedomain(win)
plt.show()
