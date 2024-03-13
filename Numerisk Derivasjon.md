
[[numeriske metoder]]


$$\huge \text{1 grad derivasjon}$$

Den enkleste metoden av alle; forlengs
$$f'(x) \approx \frac{f(x+h)-f(x)}{h}$$
Gir newton definisjonen: $$f'(x) = \lim_{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$$
```
def forward_difference(f, x, h=1e-5):

    return (f(x + h) - f(x)) / h
```

---
Baklengs
$$f'(x) \approx \frac{f(x)-f(x-h)}{h}$$

```
def backward_difference(f, x, h=1e-5):

    return (f(x) - f(x - h)) / h
```

---

Midtpunkt
$$f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$$

```
def central_difference(f, x, h=1e-5):

    return (f(x + h) - f(x - h)) / (2 * h)
```

---
$$\huge \text{2 grad derivasjon}$$

$$f''(x) \approx \frac{f(x+h) - 2 f(x) + f(x-h)}{h^2}$$

```
def second_derivative(f, x, h=1e-5):

    return (f(x + h) - 2*f(x) + f(x - h)) / h**2
```

---
$$\huge \text{Høyere grader}$$

$$ f^{(n)}(x) = \lim_{h \rightarrow 0} \frac{1}{h^n} \sum_{k=0}^n (-1)^{k+n} \left( \begin{array}{c} n \\ k \end{array} \right) f(x+kh) $$