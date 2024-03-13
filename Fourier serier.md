
[[Spektralanalyse]]

[[bølge betegnelser]]
[[Funksjoner]]

---

Vi har en funksjon $f(t)$ som er definert i intervallet $0 \lt t \lt T$ og er periodisk med perioden $T$    

$$ \text{Fourier serien kan da skrives som: } f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n  \cos (\frac{2n\pi t}{T}) + b_n \sin (\frac{2n\pi t}{T}) \right)$$
$$ \text{Eller som: } f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left ( a_n \cos (n \omega t) + b_n \sin (n \omega t) \right) $$ 
- $a_0 = \frac{2}{T} \int_0^T f(t)dt$ 
- $a_n = \frac{2}{T} \int_0^T f(t) \cdot \cos \left ( \frac{2n \pi t}{T} \right)dt$ for $n$; et positivt heltall
- $b_n = \frac{2}{T} \int_0^T f(t) \cdot \sin \left ( \frac{2n \pi t}{T} \right) dt$ for $n$; et positivt heltall


En odde funksjon vil gi en sinusrekke. Dvs. bare sinusledd
En jevn funksjon vil gi en cosinusrekke. Dvs. bare cosinusledd


---

$$ \text{for en funksjon $f(x)$ med periode på $2 \pi$: } f(x) = a_0 + \sum_{n=1}^{\infty} \left( a_n  \cos (nx) + b_n \sin (nx) \right) $$
$$ a_0 = \frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x)dx $$
$$ a_n = \frac{1}{\pi} \int^{\pi}_{-\pi}f(x) \cos (nx) dx, \ \ \ \ \ \ \ \ n=1, \ 2, \ ... $$
$$ b_n = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \sin (nx) dx, \ \ \ \ \ \ \ \ n = 1, \ 2, \ ... $$
