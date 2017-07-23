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
