# ESE 531: HW4 Problem 2

# libraries
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# part a
t_array = np.arange(0, 2.01, 0.01)

# first solved sinusoid
A1 = 2
phi1 = 2 * np.pi
w1 = 7 * np.pi / 3

x1 = [A1 * np.cos(w1 * t + phi1) for t in t_array]

# second solved sinusoid
A2 = -2
phi2 = np.pi
w2 = -np.pi / 3

x2 = [A2 * np.cos(w2 * t + phi2) for t in t_array]


# plot both solved sinusoids
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(t_array, x1, '-', label='$A=2$, $\omega=7\pi/3$, $\phi=2\pi$')
ax.plot(t_array, x2, '-', label='$A=-2$, $\omega=-\pi/3$, $\phi=\pi$')
ax.legend(loc='upper right')

major_ticks = np.arange(0, 2.1, 0.25)
minor_ticks = t_array

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


ax.set_xlabel('Time (sec)')
ax.set_ylabel('x(t)')
plt.show()

# part b

# connect points with straight lines
x_d = [2, 1, -1]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(range(3), x_d, '-')

major_ticks = np.arange(0, 2.1, 0.25)
minor_ticks = t_array

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.set_title("3 Samples Connected By Lines")
ax.set_xlabel('Time (sec)')
ax.set_ylabel('x(t)')
plt.show()

# zero-insert samples and convolve with a triangular pulse
tri_impulse = [0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2]
x_d = [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1]

lin_interp = np.convolve(x_d, tri_impulse, mode='full')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(np.linspace(-1, 3.1, len(lin_interp)), lin_interp)

major_ticks = np.linspace(-1, 3.1, len(lin_interp))

ax.set_xticks(np.arange(-1, 3.1, 0.5))

# Or if you want different settings for the grids:
ax.grid()
ax.set_title("Convolution with Triangle Impulse")
ax.set_xlabel('Time (sec)')
ax.set_ylabel('x(t)')
plt.show()

# plot x_d but connected with lines
x_d_ext = [0, 2, 1, -1, 0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(np.linspace(-1, 3.1, len(x_d_ext)), x_d_ext)

major_ticks = np.linspace(-1, 3.1, len(lin_interp))

ax.set_xticks(np.arange(-1, 3.1, 0.5))

# Or if you want different settings for the grids:
ax.grid()
ax.set_title("Samples Connected with Lines")
ax.set_xlabel('Time (sec)')
ax.set_ylabel('x(t)')
plt.show()




# fit a second-degree polynomial to the three data
def f(x, a, b, c):
    return a + (b * x) + (c * x ** 2)

popt, pcov = curve_fit(f, np.arange(3), [2, 1, -1])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(np.arange(-5, 5.01, 0.01), f(np.arange(-5, 5.01, 0.01), *popt))

major_ticks = np.arange(-5, 5.1, 1)
minor_ticks = np.arange(-5, 5.1, 0.1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.set_title("Second-Degree Polynomial Fit")
ax.set_xlabel('Time (sec)')
ax.set_ylabel('x(t)')
plt.show()

# part c

# sinc interpolator function
def sinc_interp(t, x, Ts):
    result = np.zeros_like(t)
    for i, val in enumerate(t):
        current = x[i] * np.sin(np.pi * (val - i * Ts) / Ts) / (np.pi * (val - i * Ts) * Ts)
        result = result + current
    return result

# interpolate a single point sample
t_array = np.arange(-5, 5.01, 0.01)

# generate single point sample (delta)
point_sample = np.zeros_like(t_array)
point_sample[int(len(point_sample) / 2)] = 1
Ts = 0.01

# periodic sinc
sinc_per = [np.sin(np.pi * t / Ts) / (np.pi * t / Ts) for t in t_array]

# convolve periodic sinc with delta function and plot result
point_sinc = np.convolve(point_sample, sinc_per, mode='same')

plt.plot(t_array, point_sinc)
plt.title("Reconstructed Point Sample using a Sinc Interpolation")
plt.xlabel("t")
plt.ylabel('$x_r(t)$')
plt.show()

# apply sinc interpolation to reconstruct sinusoid from part a
x_d = np.zeros_like(t_array)
x_d[int(len(x_d) / 2)] = 2
x_d[int(len(x_d) / 2) + int(1 / Ts)] = 1
x_d[int(len(x_d) / 2) + int(2 / Ts)] = -1
sinusoid_reconstruct = np.convolve(x_d, sinc_per, mode='same')

plt.plot(t_array, sinusoid_reconstruct)
plt.title("Reconstructed Sinusoid using a Sinc Interpolation")
plt.xlabel("t")
plt.ylabel('$x_r(t)$')
plt.show()




