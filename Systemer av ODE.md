[[ODE]]
[[Lineær algebra]]

$$ \huge \underline{\left ( \begin{array}{2} y'=2y+3g \\ g'=8y+27g \end{array} \right.}$$
1) skriv om til matriseform; $f'(x)=A \cdot f(x)$ $$ \frac{d}{dx} \cdot \left [ \begin{array}{2} y \\ g \end{array} \right] =  \left [ \begin{array}{2} 2 & 3 \\ 8 & 27 \end{array} \right] \cdot \left [ \begin{array}{2} y \\ g \end{array} \right]$$ hvor $f(x)$ $=$ $\left [ \begin{array}{2} y \\ g \end{array} \right]$ 
2) gjett at $f(x)= \vec{V} \cdot e^{\lambda x}$ 
3) løs derivasjonen på venstre side og del på $e^{\lambda x}$
4) Nå er likningen $A \cdot \vec{V} = \lambda \cdot \vec{V}$ (egenverdiproblem)
5) finn alle egenverdier og vektorer
   - $\lambda_1 = -1$, og $\lambda_2 = -28$
   - $\vec{V_1} = \left [ \begin{array}{2} 8 \\ 3 \end{array} \right]$, og $\vec{V_2} = \left [ \begin{array}{2} 9 \\ 1 \end{array} \right]$ 
6) den generelle løsningen kommer her på formen: $f_g(x)$ $=$ $C_1 \cdot \vec{V_1} \cdot e^{\lambda_1 x} + C_2 \cdot \vec{V_2} \cdot e^{\lambda_2 x}$


 **NB!** hvis man får komplekse $\lambda$
 1) $\lambda_1 = a+ib$, så vil $\lambda_2 = \overline{\lambda_1}$ grunnet ABC formelen, $a = -\frac{1}{2}$ 
 2) $\vec{V_1} = \left [ \begin{array}{2} 1 \\ i \end{array} \right]$, og $\vec{V_2} = \overline{\vec V_1}$ 
 3) $(A \cdot \vec{V} = \lambda \cdot \vec{V}) = (A \cdot \overline{\vec{V}} = \overline{\lambda} \cdot \overline{\vec{V}})$ derfor trengs bare et sett; $\vec V_1$ og $\lambda_2$
 4) så videre: $f(x) = C_1 \cdot Re (\vec{V} e^{\lambda x}) + C_2 Im (\vec{V} e^{\lambda x})$ $$ f(x) = C_1 \cdot Re (\vec{V} \cdot (\cos (x) + i \sin (x))) + C_2 \cdot Im (\vec{V} \cdot (\cos (x) + i \sin (x))) $$
 5) ; grunnet Euler's identitet
 6) løs opp og forenkle så har man de 2 generelle løsningene $f_g(x) = \left [ \begin{array}{2} y_g(x) \\ g_g(x) \end{array} \right]$ 

---

	