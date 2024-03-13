[[numeriske metoder]]

for å numerisk løse $f(x)$ for $x$.
$f(x)$ kan både være homogen eller inhomogen.
før man starter må alle ledd samles på venstresiden.

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

- $x_n$ er nåværende approksimering
- $x_{n+1}$ er den neste approksimeringen

man starter med et gjett, og itererer mot faktiske $x$

---
$$ \huge \text{Python}$$
```
def newtons_method(f, df, x0, tol=1e-5, max_iter=1000):

    x = x0 
    
    for _ in range(max_iter): 
        x_new = x - f(x) / df(x) 
        
        if abs(x_new - x) < tol: 
            return x_new x = x_new 
```