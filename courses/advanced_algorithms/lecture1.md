



### Date: 28 august

[Lecture pdf](lectures/1.pdf)

[Wikipedia link to De Boor's algorithm ](https://en.wikipedia.org/wiki/De_Boor%27s_algorithm)

A spline is a cubic function s:$[u_p,u_{k-p}] \in R \rightarrow R^2$ (?)

We are going to use De Boor's algorithm. One advatage is that is has local support for a given x value. This means that we don't have to compute all the splines for a x-value but only the ones that effect x. This is also an advantage in for example computer graphics. Where if we move a point the whole graph doesn't change.

A cubic spline has a basic representation:

$$s(u)=\sum_{i=0}^L d_i N^3_i(x)$$

First create the basic functions $N_i^3(x)$

We know from the second definition what $N$ is:

$$N^0_1(x):= $$









Where L = K - 2dimension of spline space,



Because we are just using a cubic spline we can use a recurrent formula.

We





We need more dots so the curve is $C^2$ smooth on the interval.



  L = dimension of spline space,
According to
N = basis function

Local control: You can move the graph in one point without a global effect.

$N^0_I(u)$ piecewise constant function.

$N^k_i(u):= \frac{u-u_{i}}{u_{i+k-1}-u_{i-1}}N_i^{k-1}(u´)$


Evaluationg splines: You dont have to evaluate the whole space only the "hot area" and the 2 splines before and after.


Notation:


$$d[U_{I-2},u_{I-1},u_{I}]\text{(blossom)}=\alpha(u)d[]$$



”
