# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:22:13 2024

@author: oskar
"""

import scipy.sparse as sp
import numpy as np
import matplotlib.pyplot as plt

m = 5
N = m + 2

Pa = -1
Pb = 1

PaV = 0
PbV =2

x = np.linspace(Pa, Pb, N)

print(x)


h = x[1] - x[0]

L = (1/h**2) * sp.diags([1, -2, 1], [-1, 0, 1], shape=(m, m))

A = L.toarray()

print(A)

x_intern = x[1:-1]

F = np.cos(np.pi * x_intern)

F[0] -= PaV / h**2
F[-1] -= PbV / h**2

print(F)

u = np.linalg.solve(A, F)

print(u)

u_full = np.hstack([PaV, u, PbV])

plt.plot(x, u_full, marker='o')

plt.grid(True)