
[[Taylors teorem]]
[[Funksjoner av flere variabler]]

når man har flere variabler er tilnærmingen på formen:
$$ P_1 (\vec{x}) = f(\vec{x}) + \nabla f(\vec{x})^T \cdot (\vec{x} - \vec{x_0}) $$
!merk at dette bare gir P_1. for P_2 blir det: 
$$ P_2(\vec{x}) = P_1(\vec{x}) + \frac{1}{2} \cdot (\vec{x} - \vec{x_0})^T \cdot H(\vec{x_0}) \cdot (\vec{x} - \vec{x_0}) $$
hvor H er hessematrisen

$$P_1 \text{ gir samtidig tangentplanet i punktet man betrakter. i 2D er punktet på formen: } (x_0, y_0, f(x_0, y_0))$$


***********
under maintenance
$$ \text{for } P_n: P_n (\vec{x}) = f(\vec{x_0}) + \sum_{k = 1}^{n} \frac{D^kf(\vec{x_0})}{k!} \cdot (\vec{x} - \vec{x_0})^k $$
****************************************


godemåten:
$$f(x, y)\text{ i punkt: } (x_0, y_0);$$ 
$$ \tiny P_2(x, y) = f(x_0, y_0) + f_x(x_0, y_0) \cdot (x - x_0) + f_y(y - y_0) + \frac{1}{2} \cdot (f_{xx} (x_0, y_0) \cdot (x - x_0)^2 + 2 \cdot f_{xy}(x_0, y_0) \cdot (x - x_0) \cdot (y - y_0) + f_{yy}(x_0, y_0) \cdot (y - y_0)^2)$$
