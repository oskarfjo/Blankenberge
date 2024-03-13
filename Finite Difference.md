1) definer diff likningen og randene
2) splitt området som skal løses for inn i et grid av punkter
3) approksimer den deriverte i alle punktene: $$ u''(x) \approx \frac{u(x + h) -2 \cdot u(x) + u(x - h)}{h^2}$$ (lagre i matrise)
4) løs for $f(x)$ delen (lagre i array)
5) løse Ax=b. den vil produsere vektor x som inneholder alle verdiene til punktene i gridet
6) plot gridet


$$ 1\text{D i python}$$
```
import scipy.sparse as sp
import numpy as np
import matplotlib.pyplot as plt

m = 5 
N = m + 2 

# rand posisjon
Pa = -1 
Pb = 1 

# rand verdi
PaV = 0 
PbV =2 

x = np.linspace(Pa, Pb, N) 

h = x[1] - x[0] 

# definerer en matrise 'L' som har alle punktene i gridet som numeriske U''(x)
L = (1/h**2) * sp.diags([1, -2, 1], [-1, 0, 1], shape=(m, m)) 
A = L.toarray() 

# løser for verdiene imellom(men ikke inkludert) randene
x_intern = x[1:-1] 
F = np.cos(np.pi * x_intern) 

# manuelt bearbeide første og siste pga metoden bruker elementet før og etter
# matrisen skal være [1, -2, 1] men den er [-2, 1] i start, og [1, -2] i slutt
F[0] -= PaV / h**2 
F[-1] -= PbV / h**2 

# løser Ax=b for x som er verdiene hvor funksjonsuttrykket er sant. u er en vektor
u = np.linalg.solve(A, F) 

# sandwicher det som ble regnet ut imellom de kjente randverdiene
u_full = np.hstack([PaV, u, PbV]) 

plt.plot(x, u_full) 
plt.grid(True)
```

