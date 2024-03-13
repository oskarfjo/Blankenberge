
[[numeriske metoder]]
[[Systemer av ODE]]


$$
\begin{align}
y' + y &= 0\\
y' &= -y = f(x, y)
\end{align}
$$

$$
\begin{align}
y_{n+1} &= y_{n} + h\cdot f(x_n, y_n)\\
y_{n+1} &= y_n - h\cdot y_n
\end{align}
$$


```
import numpy as np
import matplotlib.pyplot as plt

# Parametre for den numeriske utregningen
duration = 5 # Antall sekund til slutten av "simuleringen"
h = 0.1 # Skrittlengde

steps = int(duration/h) # Antall iterasjoner

# Klargjør arrayene x og y
x = np.linspace(0, duration, steps+1)
y = np.zeros(steps+1)

# Sett initialverdier
y[0] = 10

# Utfør eulers metode
for n in range(steps):
    y[n+1] = y[n] - h*y[n]

# Laget plot av funksjonen y(x)
plt.plot(x, y)
```