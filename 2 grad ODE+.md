
[[ODE]]

$$ \huge \underline{\overline{P(x)y'' + Q(x)y' + g(x)y = f(x)}}$$
$$ \text{ denne metoden fungerer for ODE'er av $n$'te grad}$$ 
for å finne løsningen $y_g$ må man løse for 2 svar; et homogent $y_h$ og et partikulært $y_p$
- hvis ODE'en er homogen er svaret $y_g = y_h$ 
- hvis ODE'en er inhomogen er svaret $y_g = y_h + y_p$ 

1) skriv likningen på formen vist over
2) løs for $y_h$
- $y_h = p(x) \lambda ^2 + Q(x) \lambda + g(x) = 0$ og løs for $\lambda$'ene
- det er 3 alternativer for $\lambda_1 \text{ og } \lambda_2$
  
---
  
1. $\lambda_1 \neq \lambda_2$ $\mapsto$ $y_h = \underline{C_1e^{\lambda_1 x} + C_2e^{\lambda_2 x}}$
2. $\lambda_1 = \lambda_2$ $\mapsto$ $y_h = \underline{e^{\lambda x} \cdot (C_1 + xC_2)}$ 
3. $\lambda_{1, 2} = a \pm ib$ $\mapsto$ $y_h = \underline{e^{a x} \cdot (C_1 \cos({b x}) + C_2 \sin({b x}))}$

---

5) løs for $y_p$ 
- gjetter formen som $y_p$ tar utfra $f(x)$. A, B, C, osv er ubestemte koeffisienter
  
6) $f(x)$ er et polynom av grad $n$ $\mapsto$ $y_p$ er et polynom av grad $n$ med ubestemte koeffisienter
7) $f(x)$ er eksponent $e^{k \cdot x}$ $\mapsto$ $y_p$ $=$ $Ae^{k \cdot x}$ 
8) $f(x)$ er trigonometrisk uttrykk trig($\pi 2 x$) $\mapsto$ $y_p$ $=$ $A\sin({\pi 2 x}) + B\cos({\pi 2 x})$ 
- **NB!** hvis $f(x)$ er likt et ledd i $y_h$ må man gange gjetningen med $x$ til den er ulik 
- når du har definert gjetningen $y_p$ setter man det inn i likningen:
$$ P(x) \cdot (y_p)'' + Q(x) \cdot (y_p)' + g(x) \cdot y_p = f(x)$$
- så løser man for de ubestemte koeffisientene A, B... og plugger de inn i $y_p$ 
- da har man $y_h$ og $y_p$ 
- regne ut $y_g = y_h + y_p$ med rand betingelsene for $y(x)$

---

$$\huge \underline{Eksempel}$$
