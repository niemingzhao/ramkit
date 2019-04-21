# -*- coding: utf-8 -*-

"""
Curve Fitting Functions.

>>> import ramkit as rk
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, signal, sparse, special

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def curve_fit(func, x, y, n=(1, 1), *args, **kwargs):
    """
    Curve Fitting.

    Parameters
    ----------
    func : callable
        Base model function to fit.
    x : 1d-ndarray
        Input data of x-axis.
    y : 1d-ndarray
        Input data of y-axis.
    n : 2-tuple (peak_num, param_num)
        Setting of multi-peak params.
        * 'peak_num' -- int, the guess number of peaks
        * 'param_num' -- int, the number of params of each peak
    p0 : list
        Initial guess for the params.
    bounds : 2-tuple of list
        Lower and upper bounds on params.
    method : str {'lm', 'trf', 'dogbox'}
        Method to use for optimization.
    kwargs :
        Keyword arguments passed to 'scipy.optimize.curve_fit'.

    Returns
    -------
    popt : 1d-ndarray
        Optimal values for the params so that the sum of the squared
        residuals of 'func(x, *popt) - y' is minimized.
    pcov : 2d-ndarray
        The estimated covariance of popt. To compute one standard deviation
        errors on the params use 'perr = np.sqrt(np.diag(pcov))'.

    Examples
    --------
    >>> import numpy as np
    >>> import ramkit as rk
    >>> import matplotlib.pyplot as plt
    >>> x = np.linspace(-5, 5, 100)
    >>> y = rk.lorentzian(x) + rk.gaussian(x, xc=1)
    >>> popt, pcov = rk.curve_fit(rk.gaussian, x, y, (2, 3),
    ...                           p0=[1, 0, 1, 1, 1, 1])
    >>> # popt, pcov = rk.curve_fit(rk.gaussian, x, y, (2, 3),
    ... #                           bounds=([0, -1, 0, 0, -1, 0],
    ... #                                   [1, 1, 1, 1, 1, 1]))
    >>> perr = np.sqrt(np.diag(pcov))
    >>> plt.plot(x, y, 'k')
    >>> plt.plot(x, rk.gaussian(x, *popt[:3]), 'r')
    >>> plt.plot(x, rk.gaussian(x, *popt[3:]), 'b')
    """
    s1 = 'def func_(x_,%s):args_=[tuple(i) for i in t([%s],%d)];return %s'
    s2 = ','.join(['a' + str(i) for i in range(n[0] * n[1])])
    s3 = '+'.join(['f(x_,*args_[' + str(i) + '])' for i in range(n[0])])
    s4 = {'t': lambda x, n: [x[i:i+n] for i in range(0, len(x), n)], 'f': func}
    exec(s1 % (s2, s2, n[1], s3), s4, locals())
    return optimize.curve_fit(locals()['func_'], x, y, *args, **kwargs)
