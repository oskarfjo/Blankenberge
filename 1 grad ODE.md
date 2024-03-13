
[[ODE]]
[[Separable ODE]]

$$\huge y'(x) + Ay(x) = f(x)$$
1) få likningen på riktig form; den vist over
2) definer $P(x)$, $Q(x)$, og $\mu (x)$
- $P(x) = +A$
- $Q(x) = f(x)$
- $\mu (x) = e^{\int P(x) dx}$ 
3) skriv om til $\underline{\mu(x) y' + \mu(x) P(x) y = \mu(x) Q(x)}$ siden $\mu(x) P(x) = \mu ' (x)$ gir produktregelen mulighet til å skrive som $(\mu(x) y(x))' = \mu(x) Q(x)$ 
4) integrer begge sidene; venstre derivasjon kanselleres så bare arbeid på høyre.
5) isoler $y(x)$ og bruk randbetingelse for å finne verdien til integrasjonskonstanten

$$\text{Hvorfor er } \mu(x) P(x) = \mu ' (x) ?$$
1) $\mu(x) P(x) = \mu ' (x)$
2) $P(x) = \frac{ \mu ' (x)}{\mu(x) }$ 
3) $\int P(x) dx = \int \frac{ \mu ' (x)}{\mu(x) } dx$  bruker u substitusjon som gir: $u=\mu(x)$, $u'(x)=\mu'(x)$, $\frac{du}{\mu'(x)} = dx$ 
4) $\int P(x) dx = \int \frac{ {\mu ' (x)}}{u} \frac{du}{\mu'(x)}$, $\mu'(x)$ kanselleres
5) $\int P(x) dx = \ln |u|$ $\tiny \text{konstanten er ubetydelig etter som det er integrerende faktor som er signifikant}$
6) $e^{\int P(x) dx} = u = \mu(x)$ 

---
$$\huge \underline{Eksempel}$$
$$ y' = 4y - 8 \text{, med rand: } y(1)=2 $$
$$ y' -4y = -8 $$
- $P(x)=-4$
- $Q(x)=-8$
- $\mu(x)=e^{-4x}$
$$ e^{-4x}y = -8 \int e^{-4x} dx$$
$$ e^{-4x}y = \frac{-8}{-4} e^{-4x} + c$$
$$ y(x) = 2 + c $$
$$\underbrace{\text{så rand}}$$
$$ 2 = 2 + c $$
$$\underline{\underline{y(x) = 2}}$$
