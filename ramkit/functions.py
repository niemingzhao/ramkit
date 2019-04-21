# -*- coding: utf-8 -*-

"""
Basic Mathematical Functions.

>>> import ramkit as rk
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, signal, sparse, special

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def constant(x, a=0):
    """
    Constant Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a : float
        Intercept.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    return 0 * x + a


def linear(x, a=1, b=0):
    """
    Linear Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a : float
        Slope.
    b : float
        Intercept.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    return a * x + b


def parabola(x, a=1, b=0, c=0):
    """
    Parabola Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a,b,c : float
        Coefficients.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    return a * x ** 2 + b * x + c


def cubic(x, a=1, b=0, c=0, d=0):
    """
    Cubic Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a,b,c,d : float
        Coefficients.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    return a * x ** 3 + b * x ** 2 + c * x + d


def gaussian(x, a=1, xc=0, w=1, y0=0):
    """
    Gaussian Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a : float
        Area.
    xc : float
        Center.
    w : float
        FWHM.
    y0 : float
        Base.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    sigma = w / (2 * np.sqrt(2 * np.log(2)))
    y1 = -np.power(x - xc, 2) / (2 * np.power(sigma, 2))
    return y0 + a / (sigma * np.sqrt(2 * np.pi)) * np.exp(y1)


def lorentzian(x, a=1, xc=0, w=1, y0=0):
    """
    Lorentzian Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a : float
        Area.
    xc : float
        Center.
    w : float
        FWHM.
    y0 : float
        Base.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    gamma = w / 2
    y1 = np.power(x - xc, 2) + np.power(gamma, 2)
    return y0 + a / np.pi * gamma / y1


def voigt(x, a=1, xc=0, wg=1, wl=1, y0=0):
    """
    Voigt Function.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    a : float
        Area.
    xc : float
        Center.
    wg : float
        FWHM of gaussian.
    wl : float
        FWHM of lorentzian.
    y0 : float
        Base.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    sigma, gamma = wg / (2 * np.sqrt(2 * np.log(2))), wl / 2
    y1 = special.wofz((x - xc + 1j * gamma) / (sigma * np.sqrt(2)))
    return y0 + a / (sigma * np.sqrt(2 * np.pi)) * np.real(y1)
