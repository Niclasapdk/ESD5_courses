import matplotlib.pyplot as plt
import numpy as np

# initialize delayed samples as 0
# w_i is w[n-i]
w_1 = 0
w_2 = 0
w_3 = 0

# number of samples to calculate
N = 50

y = np.zeros(N)

for i in range(N):
    if i == 0:
        x = 1
    else:
        x = 0

    w = x + 1.4590*w_1 - 0.9104*w_2 + 0.1978*w_3
    y[i] = 0.0317*w + 0.095*w_1 + 0.095*w_2 + 0.0317*w_3

    w_3 = w_2
    w_2 = w_1
    w_1 = w

plt.plot(y)
plt.title("Impulse respone")
plt.xlabel("Sample, n")
plt.ylabel("y[n]")
plt.show()
