

#### Ridge regression
 $$\text{min}_\beta||X\beta-y||_2^2+\alpha||\beta||_2^2$$
($a \geq 0$)

The ridge regression gives penalty on large $\beta_i$.

#### Lasso
$$\text{min}_\beta \frac{1}{2n_{\text{samples}}}||X\beta-y||_2^2+\alpha||\beta||_1$$
Note: $||x||_1 = \sum{|x_i|}$
Also punchises large $\beta_i$
