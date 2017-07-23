##Hello!

Fist a simple linear regression is just \\(Y = \alpha + \beta X \\). Where you try to fit a linear line to find pattern i data.

From a numerical mathematical stand point this is kinda simple but from a statistical stand point there is a lot of complicated terms that we need to get threw.

We start by the numerical and "easy" way.

If have some data points in two dimensions \\( (x_1,y_1),(x_2,y_2),...(x_n,y_n)\\). And we want to find a straight line that tries to go therw these points as good as possible like this:

![linear regression pic](linear_regression_line.png)

If we try to figure out how to get this line we get a system of linear equation (read matrix multiplication).

\\[\begin{cases} \alpha + \beta x_1 = y_1 \\\\ \alpha + \beta x_2 = y_2 \\\\ \alpha + \beta x_3 = y_3 \end{cases}\\]


We can rewrite this as a matrix:

\begin{bmatrix}
1 & x_{1}\\\\
1 & x_{2}\\\\
1 & x_{3}\\\\
1 & x_{4}\\\\
\vdots &\vdots
\end{bmatrix}\begin{bmatrix}
\alpha\\\\
\beta\\\\
\end{bmatrix}=\begin{bmatrix}
y_0\\\\
y_1\\\\
y_2\\\\
y_3\\\\
\vdots
\end{bmatrix}

As we see in the picture above so does not this equation have a solution. (If it did it all the dots would have to be lined up perfectly).

So instead we try to draw a line the fits the dots as good as possible. The numerical name for simple linear regression is "least squares" which means that you try to minimize \\(\sum(\hat{y_{i}}-y_i)\\)
where \\(y_i\\) is the true value and \\(\hat{y}_i\\) is the predicted value or the y value one predicted line for the specified \\(x_i\\)

The numerical proof of this is the following:

From the matrix equation above we have \\(X\beta=Y\\). This equation doesn't have a solution so the next best thing is to use
\\[X\hat{\beta} = Y\\] where \\(\hat{\beta}\\) is the coefficients for the least square solutions.

A side note is that we use \\(\hat{beta}\\) to be extra clear, in general they are the same thing.)

If we look at the picture below we see the purple plane. This is the solution space of A or X in our case. This means the space where X has a solution for given \\(\beta\\). As mentioned before our equation does not have a solution but the next best thing is projection of hour
 \\[X\hat{\beta}=\text{proj}_{Y}C(X)\\]

 where C(A) is the solution space (row space) of A.

![linear regression pic](leastproof.png)




\\(\\)
