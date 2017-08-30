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

### Variance of $\beta$
$$ Var(\beta)=Var\left(\frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\right)
$$

$$ Var(\beta)=\frac{1}{S_{xx}^2}Var\left(\sum(x_i-\bar{x})y_i\right)
$$
$$ Var(\beta)=\frac{S_{xx}}{S_{xx}^2}Var\left(\sum{y_i}\right)
$$
$$ Var(\beta)=\frac{n\sigma^2 S_{xx}}{S_{xx}^2}
$$


### Expected value of $\beta$
(using the top definition of $\beta$ )
$$ E(\beta)=E\left(\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{S_{xx}}\right)
$$

$$ =E\left(\frac{\sum(x_i-\bar{x})(\alpha+\beta x_i-\alpha+\beta \bar{x})}{S_{xx}}\right)
$$
$$ =E\left(\frac{\sum(x_i-\bar{x})(\beta x_i-\beta \bar{x})}{S_{xx}}\right)
$$
$$ =E\left(\beta\frac{\sum(x_i-\bar{x})(x_i- \bar{x})}{S_{xx}}\right)
$$
$$ =\hat{\beta}
$$
So $\beta$ is normally distributed because $y_i$ is a sample from a normal distribution. And here we see that $\beta$ is unbiased. (väntevärdesriktig)

## $\alpha$
If we do the same thing for $\alpha$:

$$ \alpha = \bar{y} - \beta \bar{x} $$

$$ \alpha = \bar{y} - \frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\bar{x}$$

$$ \alpha = \bar{y} - \frac{\sum(x_i-\bar{x})y_i}{S_{xx}}\bar{x}$$

$\bar{y}=\frac{1}{n}\sum y_i$


$$\alpha = \sum\frac{y_i}{n} - \frac{(x_i-\bar{x})y_i}{S_{xx}}\bar{x}$$

$$\alpha = \sum\left(\frac{1}{n} - \frac{(x_i-\bar{x})}{S_{xx}}\bar{x}\right)y_i$$


$$ Var(\alpha) = Var(\sum\left(\frac{1}{n} - \frac{(x_i-\bar{x})}{S_{xx}}\bar{x}\right)y_i)$$

$$ Var(\alpha) = \sigma^2 \sum\left(\frac{1}{n} - \frac{(x_i-\bar{x})}{nS_{xx}}\bar{x}\right)^2)$$

$$ Var(\alpha) = \sigma^2 \sum\left(\frac{1}{n^2} - 2\frac{(x_i-\bar{x})}{S_{xx}}\bar{x} + \frac{(x_i-\bar{x})^2\bar{x}^2}{S_{xx}^2}\right)$$

$$ Var(\alpha) = \sigma^2 \left(\frac{1}{n^2} - 0 + \frac{\bar{x}^2}{S_{xx}}\right)$$

$$ Var(\alpha) = \sigma^2 \left( \frac{S_{xx}+n\bar{x}^2}{nS_{xx}}\right)$$

$$ Var(\alpha) = \sigma^2 \left( \frac{\sum x_i^2}{nS_{xx}}\right)$$

$S_{xx} = \sum(x_i+\bar{x})^2=\sum x_i^2-n\bar{x}^2$
$$ E(\alpha) = \alpha  $$

Or the easy way:

$$var(\alpha)=var(\bar{Y}-\beta\bar{X})$$
$$\frac{\sigma^2}{n}+\bar{X}^2var(\beta)-Cov(\bar{Y},\beta)$$
$$\frac{\sigma^2}{n}+\bar{X}^2\frac{\sigma^2}{S_{xx}}-0$$
$$\sigma^2\left(\frac{1}{n}+\frac{\bar{X}^2}{S_{xx}}\right)$$

This may be wrong double check.



### Confidence intervals for $\alpha \text{ and } \beta$
We have the reference variable (we know that $\alpha$ and $\beta$ are normally distributed).

$$R_\alpha := \frac{\hat{\alpha}-\alpha}{s\sqrt{\frac{\sum_i x_i^2}{nS_{XX}}}}\sim t(n-2) $$

$$R_\beta := \frac{\hat{\beta}-\beta}{s\sqrt{\frac{1}{S_{XX}}}}\sim t(n-2) $$

From this we get the confidence intervals:
$$I_\alpha =\left(\hat{\alpha}\pm t_{\frac{p}{2}}(n-2)s\sqrt{\frac{\sum_i x_i^2}{nS_{xx}}} \right)$$
$$I_\beta =\left(\hat{\beta}\pm t_{\frac{p}{2}}(n-2)s\sqrt{\frac{1}{S_{xx}}} \right)$$



Also if $\sigma$ is know/unknown then we use
$t_{\frac{p}{2}}(n-2)$ / $\lambda_{\frac{p}{2}}(n-2)$. Different tests just ye google it.
