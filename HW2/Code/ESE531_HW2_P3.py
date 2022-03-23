# ESE 531, HW2 Problem 3

# libraries
import numpy as np
import matplotlib.pyplot as plt

# define constant sampling frequency
fs = 8000 # Hz

# part a
fo = 300 # Hz
T = 0.01 # sec
N =  int(fs * T)
x = np.sin([2 * np.pi * fo/fs * n for n in range(N)])

# plot x[n]
plt.stem(x)
plt.title("Sampled Sinusoid")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()

# part b

fig, axs = plt.subplots(4, 1, sharex=True)

# list of frequencies
fo_list = np.arange(100, 600, 125) # Hz
for i, f in enumerate(fo_list):
    x_f = np.sin([2 * np.pi * f/fs * n for n in range(N)])
    axs[i].stem(x_f)
    axs[i].set_ylabel(f'$x_{({f})}[n]$')

axs[3].set_xlabel('n')
plt.show()

# part c

fig2, axs2 = plt.subplots(4, 1, sharex=True)

# list of frequencies
fo_list2 = np.arange(7525, 8025, 125) # Hz
for i, f in enumerate(fo_list2):
    x_f = np.sin([2 * np.pi * f/fs * n for n in range(N)])
    axs2[i].stem(x_f)
    axs2[i].set_ylabel(f'$x_{({f})}[n]$')

axs2[3].set_xlabel('n')
plt.show()

# part d

fig3, axs3 = plt.subplots(4, 1, sharex=True)

# list of frequencies
fo_list3 = np.arange(32100, 32600, 125) # Hz
for i, f in enumerate(fo_list3):
    x_f = np.sin([2 * np.pi * f/fs * n for n in range(N)])
    axs3[i].stem(x_f)
    axs3[i].set_ylabel(f'$x_{({f})}[n]$')

axs3[3].set_xlabel('n')
plt.show()
