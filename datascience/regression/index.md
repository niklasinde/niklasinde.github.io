

## Welcome to Regression


To begin we need to understand that the different distributions ask different questions.

Simple linear regression and multivariable regression we ask to have the error (or the residuals) to normally distributed with \\( N(0,\sigma^2) \\).<br/>
So in simple linear regression we just ask the line to be in the center of the data. And in multivariable linear regression we just span this thought to higher dimensions.<br>

[Simple Linear regression](linearregression/)<br>
[Multivariable Regression](multivarregression.md)<br>

In logistic regression we ask to approximate the \\(\lambda\\) in where instead of the \\(Y_i \sim N(\alpha+\beta x_i,\sigma^2)\\), it has the distribution \\(Y_i \sim Pois(\lambda_i)\\), where \\(lambda_i\\) is something you can find in the link below.<br>

[Logistic Regression](Logisticregression.md) (also referred to as a binomial regression with log it link function)<br>

[Poisson Regression](poisson.md)<br>
[Tree regression](http://www.di.fc.ul.pt/~jpn/r/tree/tree.html) Link to another website



<table class="wikitable" style="background:white;">
<caption>Common distributions with typical uses and canonical link functions</caption>
<tbody><tr>
<th>Distribution</th>
<th>Support of distribution</th>
<th>Typical uses</th>
<th>Link name</th>
<th>Link function</th>
<th>Mean function</th>
</tr>
<tr>
<td><a href="/wiki/Normal_distribution" title="Normal distribution">Normal</a></td>
<td>real: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mo>+</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,+\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e577bfa9ed1c0f83ed643206abae3cd2f234cf9c" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:11.18ex; height:2.843ex;" alt="(-\infty ,+\infty )"></span></td>
<td>Linear-response data</td>
<td>Identity</td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mo>=</mo>
        <mi>μ<!-- μ --></mi>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\mu \,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/63238c06f9c1927aee60b40fec3adccd419cf32a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:8.483ex; height:2.676ex;" alt="\mathbf {X} {\boldsymbol {\beta }}=\mu \,\!"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>μ<!-- μ --></mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu =\mathbf {X} {\boldsymbol {\beta }}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/12c514082234f52d09595635789f474de0279b7d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:8.483ex; height:2.676ex;" alt="\mu =\mathbf {X} {\boldsymbol {\beta }}\,\!"></span></td>
</tr>
<tr>
<td><a href="/wiki/Exponential_distribution" title="Exponential distribution">Exponential</a></td>
<td rowspan="2">real: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mo>+</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (0,+\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/de77e40eb7e2582eef8a5a1da1bc027b7d9a8d6e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:8.2ex; height:2.843ex;" alt="(0,+\infty )"></span></td>
<td rowspan="2">Exponential-response data, scale parameters</td>
<td rowspan="2"><a href="/wiki/Multiplicative_inverse" title="Multiplicative inverse">Inverse</a></td>
<td rowspan="2"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mo>=</mo>
        <msup>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>1</mn>
          </mrow>
        </msup>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\mu ^{-1}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/35c753c466b330a78b576fc8727e188962cc604f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:10.83ex; height:3.176ex;" alt="{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\mu ^{-1}\,\!}"></span></td>
<td rowspan="2"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>μ<!-- μ --></mi>
        <mo>=</mo>
        <mo stretchy="false">(</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <msup>
          <mo stretchy="false">)</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>1</mn>
          </mrow>
        </msup>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu =(\mathbf {X} {\boldsymbol {\beta }})^{-1}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/77e75642db84d5f96e6c2ceb8b6c1deec1b41037" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:12.66ex; height:3.176ex;" alt="{\displaystyle \mu =(\mathbf {X} {\boldsymbol {\beta }})^{-1}\,\!}"></span></td>
</tr>
<tr>
<td><a href="/wiki/Gamma_distribution" title="Gamma distribution">Gamma</a></td>
</tr>
<tr>
<td><a href="/wiki/Inverse_Gaussian_distribution" title="Inverse Gaussian distribution">Inverse<br>
Gaussian</a></td>
<td>real: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mo>+</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (0,+\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/de77e40eb7e2582eef8a5a1da1bc027b7d9a8d6e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:8.2ex; height:2.843ex;" alt="(0,+\infty )"></span></td>
<td></td>
<td>Inverse<br>
squared</td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mo>=</mo>
        <msup>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>2</mn>
          </mrow>
        </msup>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\mu ^{-2}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0a3b87590326202b24e85ce5762989fd34bff8c2" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:10.83ex; height:3.176ex;" alt="{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\mu ^{-2}\,\!}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>μ<!-- μ --></mi>
        <mo>=</mo>
        <mo stretchy="false">(</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <msup>
          <mo stretchy="false">)</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>1</mn>
            <mrow class="MJX-TeXAtom-ORD">
              <mo>/</mo>
            </mrow>
            <mn>2</mn>
          </mrow>
        </msup>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu =(\mathbf {X} {\boldsymbol {\beta }})^{-1/2}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9f2b2781a377e3d9ed78c1b1e026fda1e8895402" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:14.319ex; height:3.343ex;" alt="{\displaystyle \mu =(\mathbf {X} {\boldsymbol {\beta }})^{-1/2}\,\!}"></span></td>
</tr>
<tr>
<td><a href="/wiki/Poisson_distribution" title="Poisson distribution">Poisson</a></td>
<td>integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo>,</mo>
        <mn>2</mn>
        <mo>,</mo>
        <mo>…<!-- … --></mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle 0,1,2,\ldots }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b1da8ed7e74b31b6314f23f122a1198c104fcaad" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:9.386ex; height:2.509ex;" alt="0,1,2,\ldots "></span></td>
<td>count of occurrences in fixed amount of time/space</td>
<td><a href="/wiki/Natural_logarithm" title="Natural logarithm">Log</a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mo>=</mo>
        <mi>ln</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mo stretchy="false">(</mo>
          <mi>μ<!-- μ --></mi>
          <mo stretchy="false">)</mo>
        </mrow>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\ln {(\mu )}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ef9f78b057c55a36d8b2516ba1f22a64f601fa1e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:12.66ex; height:2.843ex;" alt="\mathbf {X} {\boldsymbol {\beta }}=\ln {(\mu )}\,\!"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>μ<!-- μ --></mi>
        <mo>=</mo>
        <mi>exp</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mo stretchy="false">(</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="bold">X</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="bold-italic">β<!-- β --></mi>
          </mrow>
          <mo stretchy="false">)</mo>
        </mrow>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu =\exp {(\mathbf {X} {\boldsymbol {\beta }})}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b8cdcc2a7f1ac3de2da641254ab17cd120d1ce5e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; margin-right: -0.387ex; width:14.284ex; height:2.843ex;" alt="\mu =\exp {(\mathbf {X} {\boldsymbol {\beta }})}\,\!"></span></td>
</tr>
<tr>
<td><a href="/wiki/Bernoulli_distribution" title="Bernoulli distribution">Bernoulli</a></td>
<td>integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo fence="false" stretchy="false">{</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo fence="false" stretchy="false">}</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \{0,1\}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/28de5781698336d21c9c560fb1cbb3fb406923eb" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:5.736ex; height:2.843ex;" alt="\{0,1\}"></span></td>
<td>outcome of single yes/no occurrence</td>
<td rowspan="5"><a href="/wiki/Logit" title="Logit">Logit</a></td>
<td rowspan="5"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold">X</mi>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <mi mathvariant="bold-italic">β<!-- β --></mi>
        </mrow>
        <mo>=</mo>
        <mi>ln</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mrow>
            <mo>(</mo>
            <mrow class="MJX-TeXAtom-ORD">
              <mfrac>
                <mi>μ<!-- μ --></mi>
                <mrow>
                  <mn>1</mn>
                  <mo>−<!-- − --></mo>
                  <mi>μ<!-- μ --></mi>
                </mrow>
              </mfrac>
            </mrow>
            <mo>)</mo>
          </mrow>
        </mrow>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mathbf {X} {\boldsymbol {\beta }}=\ln {\left({\frac {\mu }{1-\mu }}\right)}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b1399fce891de947b987e2e8ae8abd942316a681" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; margin-right: -0.387ex; width:19.132ex; height:6.176ex;" alt="\mathbf {X} {\boldsymbol {\beta }}=\ln {\left({\frac {\mu }{1-\mu }}\right)}\,\!"></span></td>
<td rowspan="5"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>μ<!-- μ --></mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mi>exp</mi>
              <mo>⁡<!-- ⁡ --></mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">(</mo>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold">X</mi>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold-italic">β<!-- β --></mi>
                </mrow>
                <mo stretchy="false">)</mo>
              </mrow>
            </mrow>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <mi>exp</mi>
              <mo>⁡<!-- ⁡ --></mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">(</mo>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold">X</mi>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold-italic">β<!-- β --></mi>
                </mrow>
                <mo stretchy="false">)</mo>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>1</mn>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <mi>exp</mi>
              <mo>⁡<!-- ⁡ --></mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">(</mo>
                <mo>−<!-- − --></mo>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold">X</mi>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi mathvariant="bold-italic">β<!-- β --></mi>
                </mrow>
                <mo stretchy="false">)</mo>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
        <mspace width="thinmathspace"></mspace>
        <mspace width="negativethinmathspace"></mspace>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu ={\frac {\exp {(\mathbf {X} {\boldsymbol {\beta }})}}{1+\exp {(\mathbf {X} {\boldsymbol {\beta }})}}}={\frac {1}{1+\exp {(-\mathbf {X} {\boldsymbol {\beta }})}}}\,\!}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/edc5319ec8c1afe66476e8fc9c12710965ddfdca" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; margin-right: -0.387ex; width:38.306ex; height:6.509ex;" alt="\mu ={\frac {\exp {(\mathbf {X} {\boldsymbol {\beta }})}}{1+\exp {(\mathbf {X} {\boldsymbol {\beta }})}}}={\frac {1}{1+\exp {(-\mathbf {X} {\boldsymbol {\beta }})}}}\,\!"></span></td>
</tr>
<tr>
<td><a href="/wiki/Binomial_distribution" title="Binomial distribution">Binomial</a></td>
<td>integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo>,</mo>
        <mo>…<!-- … --></mo>
        <mo>,</mo>
        <mi>N</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle 0,1,\ldots ,N}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4f0dabd0eecff746a5377991354a67ea28a4e684" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:10.674ex; height:2.509ex;" alt="0,1,\ldots ,N"></span></td>
<td>count of # of "yes" occurrences out of N yes/no occurrences</td>
</tr>
<tr>
<td rowspan="2"><a href="/wiki/Categorical_distribution" title="Categorical distribution">Categorical</a></td>
<td>integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mi>K</mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [0,K)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/aa074207d3bea2e879410172ce89ba2435d37d11" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:5.866ex; height:2.843ex;" alt="[0,K)"></span></td>
<td rowspan="2">outcome of single K-way occurrence</td>
</tr>
<tr>
<td>K-vector of integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">]</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [0,1]}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/738f7d23bb2d9642bab520020873cccbef49768d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:4.705ex; height:2.843ex;" alt="[0,1]"></span>, where exactly one element in the vector has the value 1</td>
</tr>
<tr>
<td><a href="/wiki/Multinomial_distribution" title="Multinomial distribution">Multinomial</a></td>
<td><i>K</i>-vector of integer: <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mi>N</mi>
        <mo stretchy="false">]</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [0,N]}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/703d57dca548a7f9d927247c2a27b67666aebdd5" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:5.606ex; height:2.843ex;" alt="[0,N]"></span></td>
<td>count of occurrences of different types (1 .. <i>K</i>) out of <i>N</i> total <i>K</i>-way occurrences</td>
</tr>
</tbody></table>
