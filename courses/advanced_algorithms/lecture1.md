



### Date: 28 august

[Lecture pdf](lectures/1.pdf)


A spline is a cubic function s:$[u:2,u_{k-2}] \in R \rightarrow R^2$

We need more dots so the curve is $C^2$ smooth on the interval.


$$s(u)=\sum_i=0^L d_i N^3_i(u)$$ L = dimension of spline space,

N = basis function

Local control: You can move the graph in one point without a global effect.

$N^0_I(u)$ piecewise constant function.

$N^k_i(u):= \frac{u-u_{i}}{u_{i+k-1}-u_{i-1}}N_i^{k-1}(u´)$


Evaluationg splines: You dont have to evaluate the whole space only the "hot area" and the 2 splines before and after.


Notation:


$$d[U_{I-2},u_{I-1},u_{I}]\text{(blossom)}=\alpha(u)d[]$$
