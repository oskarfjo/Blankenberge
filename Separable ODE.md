
[[ODE]]
$$\huge y'=f(x)g(y)$$

1) isoler $y'$
2) skriv som $\frac{dy}{dx}$
3) separer variablene; $x$ på ene siden og $y$ på andre. dette inkluderer $dx$ og $dy$ 
4) integrer funksjonen
5) få $y(x)$ nå alene på venstresiden
6) bruk randbetingelse og finn verdien til integrasjonskonstanten

---

$$\huge \underline{\text{Eksempel}}$$
$$y'(x)=7\cdot \frac{(4+y)}{x}, \text{ med rand: }y(1)=5$$
$$\frac{dy}{dx} = 7 \cdot \frac{(4+y)}{x}$$
$$\frac{1}{4+y}dy = 7 \cdot \frac{1}{x}dx$$
$$\int \frac{1}{4+y}dy = 7 \cdot \int\frac{1}{x}dx$$
$$\ln|4+y| = 7 \cdot \ln|x| + c$$
$$e^{\ln|4+y|} = e^{7 \cdot \ln|x| + c}$$
$$4+y = x^7 \cdot c$$
$$y(x)=c \cdot x^7-4$$
$$\underbrace{\text{så rand}}$$
$$ 5 = c \cdot 1^7 - 4$$
$$ c = 9$$
$$\underline{ \underline{ y(x)= 9 \cdot x^7 - 4 }} $$
