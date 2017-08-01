
### The R function so you can try it.

First check out simple linear regression.

$$\begin{equation*}
\begin{bmatrix}
1 & x_{1,1} &x_{2,1}&x_{3,1}&\dots\\
1 & x_{1,2} &x_{2,2}&x_{3,2}&\dots\\
1 & x_{1,3} &x_{2,3}&x_{3,3}&\dots\\
1 & x_{1,4} &x_{2,4}&x_{3,4}&\dots\\
\vdots &\vdots &\vdots &\vdots& \ddots
\end{bmatrix}\begin{bmatrix}
\beta_0\\
\beta_1\\
\beta_2\\
\beta_3\\
\vdots
\end{bmatrix}=\begin{bmatrix}
y_0\\
y_1\\
y_2\\
y_3\\
\vdots
\end{bmatrix}
\end{equation*}$$

Its is the same thing as a linear regression but with more x variables.




And here we don't get $\alpha$ and $\beta$. Here we get a $\beta$ vector.

Its is the same proof as in [linear regression](http://niklasinde.github.io/datascience/regression/llinearregression/).

Here instead the estimates for $\beta$.

$$ \hat{\beta}=(X^TX)^{-1}X^TY $$
$$ =(X^TX)^{-1}X^T(X\beta+\epsilon) $$
$$=\beta +(X^TX)^{-1}X^T \epsilon$$

We know that $\hat{\beta}-\beta \sim N(0,\sigma^2(X^TX)^{-1})$.


We add the dummy variable to make the covariance matrix non singular.

Check the lectures from your course linear and logistic regression on your computer.
