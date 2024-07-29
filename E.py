import numpy as np
import matplotlib.pyplot as plt

# Parameters
f1 = 50
f2 = 120
fs = 1000  # Sampling frequency
T = 1  # Duration in seconds
t = np.linspace(0, T, fs * T, endpoint=False)  # Time vector

# Signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute FFT
S = np.fft.fft(s)
freqs = np.fft.fftfreq(len(S), 1/fs)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(freqs)//2], np.abs(S)[:len(S)//2])
plt.title('Frequency components of the signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
