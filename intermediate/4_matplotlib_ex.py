"""
Python Libraries - MatPlotLib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
https://matplotlib.org
"""

import matplotlib.pyplot as plt
import numpy as np


# def simple_plot():
#     x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
#     fig = plt.figure(figsize=(10, 5))
    
#     plt.plot(x, y, color="blue")
#     plt.scatter(x, y, color="red")
#     plt.show()

# simple_plot()


# def multiline_plot():
#     x = np.arange(-3*np.pi, 3*np.pi, 0.2)
#     y1 = np.cos(x)
#     y2 = np.sin(x)

#     plt.plot(x, y1, 'o-')
#     plt.plot(x, y2, '--')

#     plt.grid(alpha=0.5, color='gray')
#     plt.title("This is a title")
#     plt.xlabel("X label")
#     plt.ylabel("Y label")
#     plt.xlim(-5, 5)
#     plt.show()

# multiline_plot()


# def multi_plot():
#     dt = 0.03
#     t = np.arange(0, 10, dt)
#     signal1 = np.random.randn(len(t)) * 10
#     signal2 = np.random.randn(len(t)) * 10

#     fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))
    
#     axs[0].plot(t, signal1, t, signal2)
#     axs[0].set_xlim(0, 10)
#     axs[0].set_ylabel('Signals')
#     axs[0].grid(True)

#     diff = signal2 - signal1

#     axs[1].plot(t, diff, c='g')
#     axs[1].set_xlim(0, 10)
#     axs[1].set_ylabel('Difference')
#     axs[1].set_xlabel('Time')
#     axs[1].grid(True)

#     plt.show()
#     fig.savefig("./files/test.png")

# multi_plot()


# def lorenz(xyz, *, s=10, r=28, b=2.667):
#     x, y, z = xyz
#     x_dot = s*(y - x)
#     y_dot = r*x - y - x*z
#     z_dot = x*y - b*z
#     return np.array([x_dot, y_dot, z_dot])


# def lorentz_plot3D():
#     dt = 0.01
#     num_steps = 10000

#     xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
#     xyzs[0] = (0., 1., 1.05)  # Set initial values
#     # Step through "time", calculating the partial derivatives at the current point
#     # and using them to estimate the next point
#     for i in range(num_steps):
#         xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

#     # Plot
#     ax = plt.figure().add_subplot(projection='3d')

#     ax.plot(*xyzs.T, lw=0.5)
#     ax.set_xlabel("X Axis")
#     ax.set_ylabel("Y Axis")
#     ax.set_zlabel("Z Axis")
#     ax.set_title("Lorenz Attractor")

#     plt.show()

# lorentz_plot3D()

