[[Funksjoner av flere variabler]]

gradienten er stingningstallet til en funksjon i en rettning
$$\text{Gradienten kan defineres på 3 måter: } \nabla f(\vec{x}) = \left [ \begin{array}{c} \frac{\partial f}{\partial x} (\vec{x}) \\ \frac{\partial f}{\partial y} (\vec{x}) \end{array} \right] = Df(\vec{x})$$
Gradienten inneholder de rettningsderiverte i retning til enhetsvektorene
$$\vec{e_x} = \left [ \begin{array}{c} 1 \\ 0 \end{array} \right ] \text{ og } \vec{e_y} = \left [ \begin{array}{c} 0 \\ 1 \end{array} \right ]$$
$$ \text{F.eks. } D \vec{e_x}(\vec{x}) = \nabla f(x) \cdot \left [ \begin{array}{c} 1 \\ 0 \end{array} \right ] = \left [ \begin{array}{c} \frac{\partial f}{\partial x} (\vec{x}) \\ \frac{\partial f}{\partial y} (\vec{x}) \end{array} \right] \cdot \left [ \begin{array}{c} 1 \\ 0 \end{array} \right ] = \frac{\partial f}{\partial x} (\vec{x}) \text{, og tillsvarende i } \vec{e_y} \text{ rettning}$$
gradienten peker naturlig i retningen hvor stigningen er brattest.
Stigningstallet i retning u angis ved 
$$D \vec{u} (\vec{x}) = \nabla f \cdot \vec{u} = | \nabla f | \cdot | \vec{u} | \cdot \cos ( \theta )$$
theta representerer vinkelen imellom gradienten og enhetsvektoren u.
når theta er 0 peker u mot bratteste punktet (altså samme retning som gradienten)

stigningstallet regnes ut ved å ta magnituden til gradienten