"""
Python Libraries - Scipy

https://docs.scipy.org/
"""


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.stats as stats

from scipy.fft import fft, fftfreq


# def fitting():
#     def gauss(x, a, x0, sigma):
#         return a * np.exp(-(x-x0)**2/(2*sigma**2))


#     x = np.linspace(0, 10, 100)
#     y = gauss(x, 1, 5, 2)
    
#     yn = y + 0.2 * np.random.normal(size=len(x))

#     popt, pcov = curve_fit(gauss, x, yn)

#     ym = gauss(x, popt[0], popt[1], popt[2])

#     print("a =", popt[0])
#     print("x0 =", popt[1])
#     print("sigma =", popt[2])
#     print("chi2 =", stats.chisquare(f_obs=ym, f_exp=y*np.mean(ym)/np.mean(y)))


#     fig = plt.figure()
#     plt.plot(x, y, c='k', label='Function')
#     plt.scatter(x, yn)
    
#     plt.plot(x, ym, c='r', label='Best fit')
#     plt.legend()
#     plt.show()


# fitting()


# def fourier_transform():
#     N = 600
#     T = 1.0 / 800.0
#     x = np.linspace(0.0, N*T, N, endpoint=False)
#     y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    
#     xf = fftfreq(N, T)[:N//2]
#     yf = fft(y)
    
#     plt.plot(xf, 2.0 / N * np.abs(yf[0:N//2]))
#     plt.grid()
    
#     plt.show()


# fourier_transform()