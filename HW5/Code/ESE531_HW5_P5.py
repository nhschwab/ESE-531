# ESE 531: HW5 Problem 4

# Higher Order System

# libraries
import numpy as np
import matplotlib.pyplot as plt
import control
from scipy.signal import lfilter
from ESE531_HW5_P2 import gdel

# constants 
p1 = 0.9
p2 = 0.6718 + 0.6718j
p3 = 0.6718 - 0.6718j
z1 = -1
z2 = 1j
z3 = -1j
b0 = 1 / 77

# part a 

# polynomial coefficients derived by expanding pole, zero representation
sys = control.TransferFunction(np.poly((z1, z2, z3)), np.poly((p1, p2, p3)))
control.pzmap(sys, plot=True)
plt.show()

# part b
'''
function: zp2tf(p, z)

arguments:

    p: array_like of pole values
    z: array_like of zero values

return:

    Transfer Function description of impulse response as a rational function in orders of z^-1
'''

def zp2tf(z, p):

    # numerator is polynomial with zeros as roots
    num = np.poly(z)

    # denominator is polynomial with poles as roots
    den  = np.poly(p)

    return num, den

# part c

# use function zp2tf to compute impulse response 
h = np.zeros(100)
h[50] = 1

z_list = [z1, z2, z3]
p_list = [p1, p2, p3]

b, a = zp2tf(z_list, p_list)
y = lfilter(b, a, h)
n = np.arange(-50, 50, 1)

plt.stem(n, y)
plt.title('Impulse Response of System')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

# part d

# generate a 100 sample unit step signal
u_n = np.zeros(100)
u_n[50:] = 1

# step response of the system is the impulse convolved with the unit step 
step_response = np.convolve(y, u_n, mode='same')

# plot the unit step along with the system step response
fig, axs = plt.subplots(2)

axs[0].stem(n, u_n)
axs[0].set_title('Unit Step')
axs[0].set_xlabel('n')
axs[0].set_ylabel('u[n]')

axs[1].stem(n, step_response)
axs[1].set_title('Step Response of System')
axs[1].set_xlabel('n')
axs[1].set_ylabel(r'$h_u[n]$')

fig.tight_layout()

plt.show()

# another example input sequence
x_n = np.ones(100)
for i in range(100):
    if i % 2 != 0:
        x_n[i] *= -1

x_response = np.convolve(y, x_n, mode='same')

fig, axs = plt.subplots(2)

axs[0].stem(n, x_n)
axs[0].set_title('Example Sequence')
axs[0].set_xlabel('n')
axs[0].set_ylabel('x[n]')

axs[1].stem(n, x_response)
axs[1].set_title('Response of System')
axs[1].set_xlabel('n')
axs[1].set_ylabel(r'$h_x[n]$')

fig.tight_layout()

plt.show()

# part e

x_3 = np.sinc(np.arange(-1, 2, 1))
x_3response = np.convolve(y, x_3, mode='same')

fig, axs = plt.subplots(2)

axs[0].stem(np.arange(-1, 2), x_3)
axs[0].set_title('Example Sequence')
axs[0].set_xlabel('n')
axs[0].set_ylabel('x[n]')

axs[1].stem(n, x_3response)
axs[1].set_title('Response of System')
axs[1].set_xlabel('n')
axs[1].set_ylabel(r'$h_x[n]$')

fig.tight_layout()

plt.show()

# show frequency response and desired frequency representation
gd, w = gdel(y, n, 100)
plt.plot(w, np.fft.fftshift(np.abs(np.fft.fft(y, 100, norm="ortho"))), label='Frequency Response of System')

des_signal = [0.9**n for n in range(100)]
plt.plot(w, np.fft.fftshift(np.abs(np.fft.fft(des_signal, 100, norm="ortho"))), label='Desired Frequency Representation')
plt.title('Frequency Analysis')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(e^{j\omega})|$')
plt.legend()
plt.show()



