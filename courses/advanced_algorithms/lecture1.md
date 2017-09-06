



### Date: 28 august

[Lecture pdf](lectures/1.pdf)

[Wikipedia link to De Boor's algorithm ](https://en.wikipedia.org/wiki/De_Boor%27s_algorithm

[Link to first project python file](https://github.com/niklasinde/niklasinde.github.io/blob/master/courses/advanced_algorithms/projects/project1/spline_blossom.py)
A spline is a cubic function s:$[u_p,u_{k-p}] \in R \rightarrow R^2$ (?)

We are going to use De Boor's algorithm. One advatage is that is has local support for a given x value. This means that we don't have to compute all the splines for a x-value but only the ones that effect x. This is also an advantage in for example computer graphics. Where if we move a point the whole graph doesn't change.

A cubic spline has a basic representation:

$$s(u)=\sum_{i=0}^L d_i N^3_i(x)$$

First create the basic functions $N_i^3(x)$

We know from the second definition what $N$ is:

$$N^0_i(x)=
\begin{cases}
    0,& \text{if } p_{i-1}=p_{i} \\
    1,& \text{if } x \in [p_{i-1},p_i)\\
    0,& \text{else}
\end{cases}$$
and
$$N^k_i(x):= \frac{x-p_{i-1}}{p_{i+k-1}-p_{i-1}}N_i^{k-1}(x)+
\frac{p_{i+k}-x}{p_{i+k}-p_{i}}N^{k-1}_{i+1}(x)$$

Just for my self to see that the code is correct ! divide the function into two parts.


$$\frac{x-p_{i-1}}{p_{i+k-1}-p_{i-1}}N_i^{k-1}(x)$$
``` python3
((self.x-self.p[i-1])/
(self.p[i+k-1]-self.p[i-1]))*
self.rec(i,k-1,xi)
```
$$\frac{p_{i+k}-x}{p_{i+k}-p_{i}}N^{k-1}_{i+1}(x)$$
``` python3
((self.p[i+k]-self.x)/
(self.p[i+k]-self.p[i]))*
self.rec(i+1,k-1,xi)
```

Yep looks allright.


When we code this we will use the "sympy" package. This makes it able to use x as an variable. But because we do this the coding gets a bit tricky.

In this algorithm one of the cases ($1,  \text{if} x \in [p_{i-1},p_i)$). We somehow need to specify for which x we are talking about. This because one cubic spline basis function (cubic B-Spline) is only defined between $p_i \text{ and } p_{i+4}$

# HALLLÅ LOOK HERE
Check https://en.wikipedia.org/wiki/B-spline why and how dose xi affect the formal.



I solve this by creating a new list with $p_i+\frac{(p_i+p_{i+1})}{2}$. We will use this list in our regression formula just to say on which interval we are currently located.

Okey so the total python function for creating the basic functions are:


```python3
def rec(self,i,k,xi):
    """recurrence formula for b-spline"""
    #First part of the definition.
    if k == 0:
        if self.p[i-1]==self.p[i]:
            return(0)
        elif points[i-1] <= xi and xi < points[i]:
            return(1)
        else:
            return(0)      
    elif k > 0:
        n =((self.x-self.p[i-1])/(self.p[i+k-1]-self.p[i-1]))*self.rec(i,k-1,xi)+((self.p[i+k]-self.x)/(self.p[i+k]-self.p[i]))*self.rec(i+1,k-1,xi)
        return(n)
```

So this will return n which is $N^3_i(x)$. k = 3 because we want a cubic spline.

To start the recursion formula for each function we use the code:
```python3
[rec(i,3,xi[i]) for i in range(len(self.p)-4)]
```
This will give us a list with all basic functions.
























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
