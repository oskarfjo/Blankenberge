
[[numeriske metoder]]

---

**Midtpunkt**
$$ \frac{b-a}{n} \cdot (f(m_1) + f(m_2) + ...+f(m_n))$$
Hvor $m_i$ er $\frac{x_{i-1}+x_i}{2}$. i.e, splitt opp intervallet $\int_a^b$ inn i $n$ biter


```
def midtpunkt(f, a, b, n):    
    x = np.linspace(a, b, n+1)      
    dx = (b - a)/n 
    ym = f(x[0:n] + dx/2) 
    ms = np.sum(ym) * dx
    return ms
```

---

**Trapes**
$$\frac{b-a}{2n} \cdot (f(x_0) + 2 \cdot f(x_1) + 2 \cdot f(x_2) +...+ 2 \cdot f(x_{n-1}) + f(x_n))$$

```
def trapes(f, a, b, n):    
    x = np.linspace(a, b, n+1)      
    dx = (b - a)/n    
    ts = (f(x[0]) + 2*np.sum(f(x[1:n])) +  f(x[-1])) * dx/2   
    return ts
```

---

**Simpson**

 $h = \dfrac{b-a}{2n}, \qquad x_j = a+jh,\qquad$and$\qquad y_j=f(x_j)\qquad$for $j=0,\ldots,2n$
 
$$
\small
S_{2n}=\dfrac{h}{3}(y_0+4\Big(\sum_{k=1}^{n}y_{2k-1})+2(\sum_{k=1}^{n-1}y_{2k})+y_{2n})$$$$
\text{enklere forklart: }\dfrac{h}{3}(y_0+4y_1+2y_2+4y_3+\dots+2y_{2n-2}+4y_{2n-1}+y_{2n})
$$

```
def simpson(f,a,b,n):
    if (n%2 != 0):         
        print("n må være et partall når vi bruker Simpsons metode.\n")
        return None           
    
    x = np.linspace(a, b, n+1)      
    dx = (b - a)/n    
    ss = (f(x[0]) + f(x[-1]) + 4*np.sum(f(x[1::2])) + 2*np.sum(f(x[2:n:2]))) * dx/3         
    return ss
```
