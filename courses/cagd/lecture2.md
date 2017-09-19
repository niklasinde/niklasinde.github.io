### Date : 14 sept


## Splines

Bezire curves
* Have the bernstein polynomials as basis function.

* Can have multiple $y(x_i)=y(x_j)$

* Limit by the controlpoints

* "Less wiggle" then the control points polygon.

* Derivative easy to calculate.

* Does not have local support.

B-spline curves.

* control points

* basis functions

* Have knots because one basis is only defined for a specific knot.

A spline is a piecewise function with some continuous conditions.

B-spline is a piecewise basis function.

Cox-de Boor formula:

$$N_i^k(x)=\frac{x-p_i}{p_{i-k+1}-p_{i}}N_i^{k-1}(x)+
\frac{p_{i+k+1}-x}{p_{i+k+1}-p_{i+1}}N_{i+1}^{k-1}(x)$$



$$N_i^0(x)= \begin{cases}
    1 \text{ if } x\in[p_i,p_{i+1}) \\
    0 \text{ otherwise}
\end{cases}$$
