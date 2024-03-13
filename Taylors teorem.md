[[Matte 2]]

[[Taylors teorem med flere variabler]]

$$T_n(x) = \sum_{k=0}^{n} \left( \frac{1}{k!} \frac{d^k f}{dx^k} (x-x_0)^k \right)$$
Taylors polynom. Funksjonen deriveres k ganger, og hver deriverte er et nytt ledd. Hvert ledd deles på fakuliteten til graden av derivasjon, og ganges med x(variabel) - x_0(punktet man betrakter) som er opphøyd i graden av derivasjon. Desto større k er; Desto mere nøyaktig tilnerming av grafen. Jo lengere unna punktet  x_0 man beverer seg; jo mindre nøyaktig blir verdien. For å regne ut størrelsen på Erroren, brukes:
$$ E(x) = |f(x)-T(x)|$$
det er en forenklet versjon av: $$E(x)=\frac{f^{(n+1)}(ξ)}{(n+1)!}​(x−x_0​)^{n+1}$$
hvor ξ er et tall mellom x og x_0, avhengig av funksjonen og intervallet. #middelverdisettningen
for å finne ξ, tilnærmer man: $$R_n(x) \le \frac{1}{(n+1)!} \cdot (x - x_0)^{(n+1)} \text{,   maks } f^{(n+1)}(a) \text{ hvor a er et tall mellom } x \text{ og } x_0$$ 