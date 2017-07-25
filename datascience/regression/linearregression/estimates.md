# Overkill

### What is the distributions of alpha and beta


$\alpha \text{ and } \beta$?

$\alpha = \bar{y}-\frac{S_{xy}}{S_{xx}}\bar{x}$

Why is $\alpha \text{and} \beta$ normally distributed?

We know that $\sum{(x_i-\bar{x})}$ and:

$$
\beta = \frac{S_{xy}}{S_{xx}}
$$
$$= \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{S_{xx}}
$$

$$= \frac{\sum(x_i-\bar{x})y_i-\sum(x_i-\bar{x})\bar{y})}{S_{xx}}
$$

$$=
\frac{\sum(x_i-\bar{x})y_i-\bar{y}\sum(x_i-\bar{x})}{S_{xx}}
$$

$$=
\frac{\sum(x_i-\bar{x})y_i}{S_{xx}}
$$
So $\beta$ is normally distributed because $y_i$ is a sample from a normal distribution.

$$ Var(\beta)=Var\left(\frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\right)
$$

$$ Var(\beta)=\frac{1}{S_{xx}^2}Var\left(\sum(x_i-\bar{x})y_i\right)
$$
$$ Var(\beta)=\frac{S_{xx}}{S_{xx}^2}Var\left(\sum{y_i}\right)
$$
$$ Var(\beta)=\frac{n\sigma^2 S_{xx}}{S_{xx}^2}
$$

$$ E(\beta)=E\left(\frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\right)
$$
$$ =E\left(\frac{\sum(x_i-\bar{x})\alpha+\beta x_i}{S_{xx}}\right)
$$

$$ =E\left(\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{S_{xx}}\right)
$$

$$ =E\left(\frac{\sum(x_i-\bar{x})(\alpha+\beta x_i-\alpha+\beta \bar{x})}{S_{xx}}\right)
$$
$$ =E\left(\frac{\sum(x_i-\bar{x})(\beta x_i-\beta \bar{x})}{S_{xx}}\right)
$$
$$ =E\left(\beta\frac{\sum(x_i-\bar{x})(x_i- \bar{x})}{S_{xx}}\right)
$$
$$ =\beta
$$
So $\beta$ is normally distributed because $y_i$ is a sample from a normal distribution.

If we do the same thing for $ \alpha $

$$ \alpha = \bar{y} - \beta \bar{x} $$

$$ \alpha = \bar{y} - \frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\bar{x}$$

$$ \alpha = \bar{y} - \frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\bar{x}$$


$$ Var(\alpha) =  $$

$$ E(\alpha) =  $$



Kolla boken och kolla share latex 1.2.4.
