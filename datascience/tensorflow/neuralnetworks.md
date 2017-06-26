
Put in the latex code for the thing you have written on your paper.


## How do neural networks work?
If we start by looking a the simplest examples of a ANN: inputs with no hidden layer and no activation function (fully connected layer)

![neuralregression](neuralregression.png)

We get:

\\[ \begin{equation*}
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix}\begin{bmatrix}
\w_{1}& \w_{2}&\w_{3}
\end{bmatrix}=
x_{1}\w_{1}+x_{2}\w_{2}+x_{3}\w_{3}
\end{equation*} \\]

So here we see that we get the same equation as a multivariable linear regression.









## Activation functions.
<table class="wikitable sortable jquery-tablesorter">
<thead><tr>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Plot</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Equation</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Derivative" title="Derivative">Derivative</a> (with respect to <i>x</i>)</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Interval_(mathematics)#Notations_for_intervals" title="Interval (mathematics)">Range</a></th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Smoothness#Order_of_continuity" title="Smoothness">Order of continuity</a></th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Monotonic_function" title="Monotonic function">Monotonic</a></th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Derivative Monotonic</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Approximates identity near the origin</th>
</tr></thead><tbody>
<tr>
<td><a href="/wiki/Identity_function" title="Identity function">Identity</a></td>
<td><a href="/wiki/File:Activation_identity.svg" class="image"><img alt="Activation identity.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Activation_identity.svg/120px-Activation_identity.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Activation_identity.svg/180px-Activation_identity.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Activation_identity.svg/240px-Activation_identity.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>x</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=x}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/f690285952308aa49e3c6aac892df31cad6d1b06" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:8.908ex; height:2.843ex;" alt="f(x)=x"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1f82687d38aa641f513d166b138923a84d7aae86" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.475ex; height:3.009ex;" alt="{\displaystyle f'(x)=1}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td><a href="/wiki/Heaviside_step_function" title="Heaviside step function">Binary step</a></td>
<td><a href="/wiki/File:Activation_binary_step.svg" class="image"><img alt="Activation binary step.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Activation_binary_step.svg/120px-Activation_binary_step.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Activation_binary_step.svg/180px-Activation_binary_step.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Activation_binary_step.svg/240px-Activation_binary_step.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/57c710d836f45b21ac5314fc64f0a117c621cc3b" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:24.331ex; height:6.176ex;" alt="{\displaystyle f(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≠<!-- ≠ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mo>?</mo>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>=</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x\neq 0\\?&amp;{\mbox{for}}&amp;x=0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/99761eb4566d128e38329db394513f3a0a8e78e5" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:25.065ex; height:6.176ex;" alt="{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x\neq 0\\?&amp;{\mbox{for}}&amp;x=0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>1</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{-1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fbeead216a363d09a6d0a05e192bdc3e7ed1067f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:4.156ex; height:2.676ex;" alt="{\displaystyle C^{-1}}"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td><a href="/wiki/Logistic_function" title="Logistic function">Logistic</a> (a.k.a. Soft step)</td>
<td><a href="/wiki/File:Activation_logistic.svg" class="image"><img alt="Activation logistic.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Activation_logistic.svg/120px-Activation_logistic.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Activation_logistic.svg/180px-Activation_logistic.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Activation_logistic.svg/240px-Activation_logistic.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>1</mn>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <msup>
                <mi>e</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mo>−<!-- − --></mo>
                  <mi>x</mi>
                </mrow>
              </msup>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)={\frac {1}{1+e^{-x}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/faaa0c014ae28ac67db5c49b3f3e8b08415a3f2b" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.005ex; width:15.988ex; height:5.343ex;" alt="{\displaystyle f(x)={\frac {1}{1+e^{-x}}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo stretchy="false">(</mo>
        <mn>1</mn>
        <mo>−<!-- − --></mo>
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=f(x)(1-f(x))}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/50a861269c68b1f1b973155fa40531d83c54c562" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:23.075ex; height:3.009ex;" alt="{\displaystyle f'(x)=f(x)(1-f(x))}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (0,1)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c79c6838e423c1ed3c7ea532a56dc9f9dae8290b" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:5.22ex; height:2.843ex;" alt="(0,1)"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td><a href="/wiki/Hyperbolic_function#Hyperbolic_tangent" title="Hyperbolic function">TanH</a></td>
<td><a href="/wiki/File:Activation_tanh.svg" class="image"><img alt="Activation tanh.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Activation_tanh.svg/120px-Activation_tanh.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Activation_tanh.svg/180px-Activation_tanh.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Activation_tanh.svg/240px-Activation_tanh.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>tanh</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>2</mn>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <msup>
                <mi>e</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mo>−<!-- − --></mo>
                  <mn>2</mn>
                  <mi>x</mi>
                </mrow>
              </msup>
            </mrow>
          </mfrac>
        </mrow>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\tanh(x)={\frac {2}{1+e^{-2x}}}-1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/48851c215e3c5b9dac76a25d4c358b9a2f7c137f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.338ex; width:31.814ex; height:5.676ex;" alt="{\displaystyle f(x)=\tanh(x)={\frac {2}{1+e^{-2x}}}-1}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mn>1</mn>
        <mo>−<!-- − --></mo>
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <msup>
          <mo stretchy="false">)</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=1-f(x)^{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b371c445bf1130914d25b1995d853ac0e27bc956" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:17.847ex; height:3.176ex;" alt="{\displaystyle f'(x)=1-f(x)^{2}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-1,1)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e120a3bd60fc89b495dd7ef6039465b7e6a703b1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:7.039ex; height:2.843ex;" alt="(-1,1)"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td><a href="/wiki/Inverse_trigonometric_functions" title="Inverse trigonometric functions">ArcTan</a></td>
<td><a href="/wiki/File:Activation_arctan.svg" class="image"><img alt="Activation arctan.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Activation_arctan.svg/120px-Activation_arctan.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Activation_arctan.svg/180px-Activation_arctan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Activation_arctan.svg/240px-Activation_arctan.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <msup>
          <mi>tan</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <mn>1</mn>
          </mrow>
        </msup>
        <mo>⁡<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\tan ^{-1}(x)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/068766282e38cec749b06698a55608f3a5821b19" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:16.477ex; height:3.176ex;" alt="{\displaystyle f(x)=\tan ^{-1}(x)}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>1</mn>
            <mrow>
              <msup>
                <mi>x</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msup>
              <mo>+</mo>
              <mn>1</mn>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)={\frac {1}{x^{2}+1}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d37bfaab02905f8eb159b83995c9b0c501c978bb" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.338ex; width:15.564ex; height:5.676ex;" alt="{\displaystyle f'(x)={\frac {1}{x^{2}+1}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow>
          <mo>(</mo>
          <mo>−<!-- − --></mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mfrac>
              <mi>π<!-- π --></mi>
              <mn>2</mn>
            </mfrac>
          </mrow>
          <mo>,</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mfrac>
              <mi>π<!-- π --></mi>
              <mn>2</mn>
            </mfrac>
          </mrow>
          <mo>)</mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \left(-{\frac {\pi }{2}},{\frac {\pi }{2}}\right)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/05c407a8d430e4361ca9ff6f154740f8bf5bfc2e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.838ex; width:10.017ex; height:4.843ex;" alt="{\displaystyle \left(-{\frac {\pi }{2}},{\frac {\pi }{2}}\right)}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td>Softsign <sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup><sup id="cite_ref-8" class="reference"><a href="#cite_note-8">[8]</a></sup></td>
<td><a href="/wiki/File:Activation_softsign.png" class="image"><img alt="Activation softsign.png" src="//upload.wikimedia.org/wikipedia/commons/3/38/Activation_softsign.png" width="120" height="60" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mi>x</mi>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">|</mo>
              </mrow>
              <mi>x</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">|</mo>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)={\frac {x}{1+|x|}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4735c7d34e544299cbbfdb4f388391627f186658" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:15.083ex; height:5.509ex;" alt="{\displaystyle f(x)={\frac {x}{1+|x|}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>1</mn>
            <mrow>
              <mo stretchy="false">(</mo>
              <mn>1</mn>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">|</mo>
              </mrow>
              <mi>x</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mo stretchy="false">|</mo>
              </mrow>
              <msup>
                <mo stretchy="false">)</mo>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msup>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)={\frac {1}{(1+|x|)^{2}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b5745ed0c96af00d5196d508712fb0fc52256cd2" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:18.709ex; height:6.009ex;" alt="{\displaystyle f'(x)={\frac {1}{(1+|x|)^{2}}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-1,1)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e120a3bd60fc89b495dd7ef6039465b7e6a703b1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:7.039ex; height:2.843ex;" alt="(-1,1)"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/bd24bae0d7570018e828e19851902c09c618af91" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^{1}"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td><a href="/wiki/Rectifier_(neural_networks)" title="Rectifier (neural networks)">Rectified linear unit</a> (ReLU)<sup id="cite_ref-9" class="reference"><a href="#cite_note-9">[9]</a></sup></td>
<td><a href="/wiki/File:Activation_rectified_linear.svg" class="image"><img alt="Activation rectified linear.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_rectified_linear.svg/120px-Activation_rectified_linear.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_rectified_linear.svg/180px-Activation_rectified_linear.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_rectified_linear.svg/240px-Activation_rectified_linear.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8d1e78eaf8445e3c1a9d48229abb921a61f30bad" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:24.498ex; height:6.176ex;" alt="{\displaystyle f(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/29ee90b67c01654d3efba98c6fd13d21f75855f1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:25.065ex; height:6.176ex;" alt="{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [0,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8dc2d914c2df66bc0f7893bfb8da36766650fe47" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:6.124ex; height:2.843ex;" alt="[0,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>Leaky rectified linear unit (Leaky ReLU)<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">[10]</a></sup></td>
<td><a href="/wiki/File:Activation_prelu.svg" class="image"><img alt="Activation prelu.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/120px-Activation_prelu.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/180px-Activation_prelu.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/240px-Activation_prelu.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0.01</mn>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\left\{{\begin{array}{rcl}0.01x&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d4a5be41d665e256098d309cf8fcb99fb3cd4e52" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:28.674ex; height:6.176ex;" alt="{\displaystyle f(x)=\left\{{\begin{array}{rcl}0.01x&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0.01</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0.01&amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/f35d0144e45dd5fe7fc7677e0d3fd4235f365acf" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:28.068ex; height:6.176ex;" alt="{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0.01&amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>Parameteric rectified linear unit (PReLU)<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup></td>
<td><a href="/wiki/File:Activation_prelu.svg" class="image"><img alt="Activation prelu.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/120px-Activation_prelu.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/180px-Activation_prelu.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/240px-Activation_prelu.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha x&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a8146769783017d86488729d231df66e769e1545" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:28.538ex; height:6.176ex;" alt="{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha x&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha &amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2ab46a9d19a6497d83238d82271b49edc95b2ec7" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:27.932ex; height:6.176ex;" alt="{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha &amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>≥<!-- ≥ --></mo>
        <mn>0</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha \geq 0}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d9e01f6a4360f062e662779cb235d41c7c68a557" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:5.78ex; height:2.509ex;" alt="\alpha \geq 0"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>=</mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha =1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/03d67a45a44be8b8f15e99b7def2b0cf0aba1717" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:5.78ex; height:2.176ex;" alt="\alpha =1"></span></td>
</tr>
<tr>
<td>Randomized leaky rectified linear unit (RReLU)<sup id="cite_ref-12" class="reference"><a href="#cite_note-12">[12]</a></sup></td>
<td><a href="/wiki/File:Activation_prelu.svg" class="image"><img alt="Activation prelu.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/120px-Activation_prelu.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/180px-Activation_prelu.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Activation_prelu.svg/240px-Activation_prelu.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha x&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a8146769783017d86488729d231df66e769e1545" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:28.538ex; height:6.176ex;" alt="{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha x&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span><sup class="reference plainlinks nourlexpansion" id="ref_alpha_random"><a class="external autonumber" href="//en.wikipedia.org/wiki/Activation_function#endnote_alpha_random">[1]</a></sup></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha &amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2ab46a9d19a6497d83238d82271b49edc95b2ec7" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:27.932ex; height:6.176ex;" alt="{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha &amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>Exponential linear unit (ELU)<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">[13]</a></sup></td>
<td><a href="/wiki/File:Activation_elu.svg" class="image"><img alt="Activation elu.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Activation_elu.svg/120px-Activation_elu.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Activation_elu.svg/180px-Activation_elu.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Activation_elu.svg/240px-Activation_elu.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo stretchy="false">(</mo>
                  <msup>
                    <mi>e</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>x</mi>
                    </mrow>
                  </msup>
                  <mo>−<!-- − --></mo>
                  <mn>1</mn>
                  <mo stretchy="false">)</mo>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha (e^{x}-1)&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a0bf7be2dfe619a4f237bf592abf27a2e51791f0" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:35.326ex; height:6.176ex;" alt="{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}\alpha (e^{x}-1)&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>f</mi>
                  <mo stretchy="false">(</mo>
                  <mi>α<!-- α --></mi>
                  <mo>,</mo>
                  <mi>x</mi>
                  <mo stretchy="false">)</mo>
                  <mo>+</mo>
                  <mi>α<!-- α --></mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}f(\alpha ,x)+\alpha &amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/13ce555ecd376f6126b78e323b4064a8ed4133fb" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:37.785ex; height:6.176ex;" alt="{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}f(\alpha ,x)+\alpha &amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\alpha ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9a966cc9f5c4412bfc563ac9790d9ed43177bfdd" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:8.525ex; height:2.843ex;" alt="{\displaystyle (-\alpha ,\infty )}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/bd24bae0d7570018e828e19851902c09c618af91" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^{1}"></span> when<br>
<span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>=</mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha =1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/03d67a45a44be8b8f15e99b7def2b0cf0aba1717" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:5.78ex; height:2.176ex;" alt="\alpha =1"></span>, otherwise <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>≥<!-- ≥ --></mo>
        <mn>0</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha \geq 0}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d9e01f6a4360f062e662779cb235d41c7c68a557" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:5.78ex; height:2.509ex;" alt="\alpha \geq 0"></span></td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mn>0</mn>
        <mo>≤<!-- ≤ --></mo>
        <mi>α<!-- α --></mi>
        <mo>≤<!-- ≤ --></mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle 0\leq \alpha \leq 1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9184b6c2088ccc2e9ac06bfb0964e264c9f6ba53" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:10.062ex; height:2.509ex;" alt="0 \leq \alpha \leq 1"></span></td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>=</mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha =1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/03d67a45a44be8b8f15e99b7def2b0cf0aba1717" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:5.78ex; height:2.176ex;" alt="\alpha =1"></span></td>
</tr>
<tr>
<td>Scaled exponential linear unit (SELU)<sup id="cite_ref-14" class="reference"><a href="#cite_note-14">[14]</a></sup></td>
<td></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>λ<!-- λ --></mi>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo stretchy="false">(</mo>
                  <msup>
                    <mi>e</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>x</mi>
                    </mrow>
                  </msup>
                  <mo>−<!-- − --></mo>
                  <mn>1</mn>
                  <mo stretchy="false">)</mo>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(\alpha ,x)=\lambda \left\{{\begin{array}{rcl}\alpha (e^{x}-1)&amp;{\mbox{for}}&amp;x&lt;0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/64fb433cb7f768ceb3e67a87ed713fd94ba97177" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:37.079ex; height:6.176ex;" alt="{\displaystyle f(\alpha ,x)=\lambda \left\{{\begin{array}{rcl}\alpha (e^{x}-1)&amp;{\mbox{for}}&amp;x<0\\x&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span>
<p>with <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>λ<!-- λ --></mi>
        <mo>=</mo>
        <mn>1.0507</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \lambda =1.0507}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/740e4b3506d22e67bfc7bfd3e995d53bb81b3327" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:10.996ex; height:2.176ex;" alt="{\displaystyle \lambda =1.0507}"></span> and <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>=</mo>
        <mn>1.67326</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha =1.67326}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/169a7cbcf6cf284fa0e53c32238fa079f5147325" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:12.302ex; height:2.176ex;" alt="{\displaystyle \alpha =1.67326}"></span></p>
</td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>λ<!-- λ --></mi>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mi>f</mi>
                  <mo stretchy="false">(</mo>
                  <mi>α<!-- α --></mi>
                  <mo>,</mo>
                  <mi>x</mi>
                  <mo stretchy="false">)</mo>
                  <mo>+</mo>
                  <mi>α<!-- α --></mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(\alpha ,x)=\lambda \left\{{\begin{array}{rcl}f(\alpha ,x)+\alpha &amp;{\mbox{for}}&amp;x&lt;0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/165d6c55490ff670f5f945574a20b2ba773ba0eb" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:39.538ex; height:6.176ex;" alt="{\displaystyle f'(\alpha ,x)=\lambda \left\{{\begin{array}{rcl}f(\alpha ,x)+\alpha &amp;{\mbox{for}}&amp;x<0\\1&amp;{\mbox{for}}&amp;x\geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi>λ<!-- λ --></mi>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\lambda \alpha ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e1357562409324a8c59d68435f87b4acb04d2045" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.891ex; height:2.843ex;" alt="{\displaystyle (-\lambda \alpha ,\infty )}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>S-shaped rectified linear activation unit (SReLU)<sup id="cite_ref-15" class="reference"><a href="#cite_note-15">[15]</a></sup></td>
<td></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>f</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <msub>
              <mi>t</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>l</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>a</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>l</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>t</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>r</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>a</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>r</mi>
              </mrow>
            </msub>
          </mrow>
        </msub>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                  <mo>+</mo>
                  <msub>
                    <mi>a</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                  <mo stretchy="false">(</mo>
                  <mi>x</mi>
                  <mo>−<!-- − --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                  <mo stretchy="false">)</mo>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≤<!-- ≤ --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                  <mo>&lt;</mo>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                  <mo>+</mo>
                  <msub>
                    <mi>a</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                  <mo stretchy="false">(</mo>
                  <mi>x</mi>
                  <mo>−<!-- − --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                  <mo stretchy="false">)</mo>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f_{t_{l},a_{l},t_{r},a_{r}}(x)=\left\{{\begin{array}{rcl}t_{l}+a_{l}(x-t_{l})&amp;{\mbox{for}}&amp;x\leq t_{l}\\x&amp;{\mbox{for}}&amp;t_{l}&lt;x&lt;t_{r}\\t_{r}+a_{r}(x-t_{r})&amp;{\mbox{for}}&amp;x\geq t_{r}\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4c61d59cfbbc6e72c8bef861b0ef61a558f910b2" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.171ex; width:50.708ex; height:9.509ex;" alt="{\displaystyle f_{t_{l},a_{l},t_{r},a_{r}}(x)=\left\{{\begin{array}{rcl}t_{l}+a_{l}(x-t_{l})&amp;{\mbox{for}}&amp;x\leq t_{l}\\x&amp;{\mbox{for}}&amp;t_{l}<x<t_{r}\\t_{r}+a_{r}(x-t_{r})&amp;{\mbox{for}}&amp;x\geq t_{r}\end{array}}\right.}"></span><br>
<span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>t</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>l</mi>
          </mrow>
        </msub>
        <mo>,</mo>
        <msub>
          <mi>a</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>l</mi>
          </mrow>
        </msub>
        <mo>,</mo>
        <msub>
          <mi>t</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>r</mi>
          </mrow>
        </msub>
        <mo>,</mo>
        <msub>
          <mi>a</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>r</mi>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t_{l},a_{l},t_{r},a_{r}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c025e6fb3b285e27e42f0d9e1b15a9e9d2e8ab44" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:10.736ex; height:2.343ex;" alt="{\displaystyle t_{l},a_{l},t_{r},a_{r}}"></span> are parameters.</td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msubsup>
          <mi>f</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <msub>
              <mi>t</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>l</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>a</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>l</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>t</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>r</mi>
              </mrow>
            </msub>
            <mo>,</mo>
            <msub>
              <mi>a</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>r</mi>
              </mrow>
            </msub>
          </mrow>
          <mo>′</mo>
        </msubsup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <msub>
                    <mi>a</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≤<!-- ≤ --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>l</mi>
                    </mrow>
                  </msub>
                  <mo>&lt;</mo>
                  <mi>x</mi>
                  <mo>&lt;</mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <msub>
                    <mi>a</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≥<!-- ≥ --></mo>
                  <msub>
                    <mi>t</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>r</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'_{t_{l},a_{l},t_{r},a_{r}}(x)=\left\{{\begin{array}{rcl}a_{l}&amp;{\mbox{for}}&amp;x\leq t_{l}\\1&amp;{\mbox{for}}&amp;t_{l}&lt;x&lt;t_{r}\\a_{r}&amp;{\mbox{for}}&amp;x\geq t_{r}\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/81516df76356e5d6bb3def9bd51ad0ae28e0ea3a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.005ex; width:38.174ex; height:9.176ex;" alt="{\displaystyle f'_{t_{l},a_{l},t_{r},a_{r}}(x)=\left\{{\begin{array}{rcl}a_{l}&amp;{\mbox{for}}&amp;x\leq t_{l}\\1&amp;{\mbox{for}}&amp;t_{l}<x<t_{r}\\a_{r}&amp;{\mbox{for}}&amp;x\geq t_{r}\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>Adaptive piecewise linear (APL) <sup id="cite_ref-16" class="reference"><a href="#cite_note-16">[16]</a></sup></td>
<td></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mo movablelimits="true" form="prefix">max</mo>
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>+</mo>
        <munderover>
          <mo>∑<!-- ∑ --></mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
            <mo>=</mo>
            <mn>1</mn>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>S</mi>
          </mrow>
        </munderover>
        <msubsup>
          <mi>a</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>i</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
          </mrow>
        </msubsup>
        <mo movablelimits="true" form="prefix">max</mo>
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mo>−<!-- − --></mo>
        <mi>x</mi>
        <mo>+</mo>
        <msubsup>
          <mi>b</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>i</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
          </mrow>
        </msubsup>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\max(0,x)+\sum _{s=1}^{S}a_{i}^{s}\max(0,-x+b_{i}^{s})}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/56b625a6deecad31eb06f22e30b922b132c5cd01" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.005ex; width:42.988ex; height:7.343ex;" alt="{\displaystyle f(x)=\max(0,x)+\sum _{s=1}^{S}a_{i}^{s}\max(0,-x+b_{i}^{s})}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>H</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>−<!-- − --></mo>
        <munderover>
          <mo>∑<!-- ∑ --></mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
            <mo>=</mo>
            <mn>1</mn>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>S</mi>
          </mrow>
        </munderover>
        <msubsup>
          <mi>a</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>i</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
          </mrow>
        </msubsup>
        <mi>H</mi>
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi>x</mi>
        <mo>+</mo>
        <msubsup>
          <mi>b</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>i</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>s</mi>
          </mrow>
        </msubsup>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=H(x)-\sum _{s=1}^{S}a_{i}^{s}H(-x+b_{i}^{s})}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/927452044470657f540f8cb073f8f9f3b750a854" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.005ex; width:34.334ex; height:7.343ex;" alt="{\displaystyle f'(x)=H(x)-\sum _{s=1}^{S}a_{i}^{s}H(-x+b_{i}^{s})}"></span><sup class="reference plainlinks nourlexpansion" id="ref_heaviside"><a class="external autonumber" href="//en.wikipedia.org/wiki/Activation_function#endnote_heaviside">[2]</a></sup></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7c14274cad45f7c22b662e7a4e56b1db052883d1" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.87ex; height:2.676ex;" alt="C^0"></span></td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>SoftPlus<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">[17]</a></sup></td>
<td><a href="/wiki/File:Activation_softplus.svg" class="image"><img alt="Activation softplus.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Activation_softplus.svg/120px-Activation_softplus.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Activation_softplus.svg/180px-Activation_softplus.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Activation_softplus.svg/240px-Activation_softplus.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>ln</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mn>1</mn>
        <mo>+</mo>
        <msup>
          <mi>e</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>x</mi>
          </mrow>
        </msup>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\ln(1+e^{x})}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/f21f3d1e2c67c5c2d2085e384512bc737c8e14af" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:17.656ex; height:2.843ex;" alt="{\displaystyle f(x)=\ln(1+e^{x})}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mn>1</mn>
            <mrow>
              <mn>1</mn>
              <mo>+</mo>
              <msup>
                <mi>e</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mo>−<!-- − --></mo>
                  <mi>x</mi>
                </mrow>
              </msup>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)={\frac {1}{1+e^{-x}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7f9e624f08baaf2b5886fc69c1162b8caf79f622" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.005ex; width:16.722ex; height:5.343ex;" alt="{\displaystyle f'(x)={\frac {1}{1+e^{-x}}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (0,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/da17102e4ed0886686094ee531df040d2e86352a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:6.382ex; height:2.843ex;" alt="(0,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td>Bent identity</td>
<td><a href="/wiki/File:Activation_bent_identity.svg" class="image"><img alt="Activation bent identity.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Activation_bent_identity.svg/120px-Activation_bent_identity.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Activation_bent_identity.svg/180px-Activation_bent_identity.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Activation_bent_identity.svg/240px-Activation_bent_identity.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <msup>
                    <mi>x</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msup>
                  <mo>+</mo>
                  <mn>1</mn>
                </msqrt>
              </mrow>
              <mo>−<!-- − --></mo>
              <mn>1</mn>
            </mrow>
            <mn>2</mn>
          </mfrac>
        </mrow>
        <mo>+</mo>
        <mi>x</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)={\frac {{\sqrt {x^{2}+1}}-1}{2}}+x}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c4365ebef6b1e8e4521ab1df8b640e27edf9557c" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.838ex; width:25.379ex; height:6.343ex;" alt="{\displaystyle f(x)={\frac {{\sqrt {x^{2}+1}}-1}{2}}+x}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mi>x</mi>
            <mrow>
              <mn>2</mn>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <msup>
                    <mi>x</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msup>
                  <mo>+</mo>
                  <mn>1</mn>
                </msqrt>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
        <mo>+</mo>
        <mn>1</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)={\frac {x}{2{\sqrt {x^{2}+1}}}}+1}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/81d4ca91d2f4e2c53745ec90a7d6cc34dde33978" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.338ex; width:23.095ex; height:6.176ex;" alt="{\displaystyle f'(x)={\frac {x}{2{\sqrt {x^{2}+1}}}}+1}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td>SoftExponential <sup id="cite_ref-18" class="reference"><a href="#cite_note-18">[18]</a></sup></td>
<td><a href="/wiki/File:Activation_soft_exponential.svg" class="image"><img alt="Activation soft exponential.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Activation_soft_exponential.svg/120px-Activation_soft_exponential.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Activation_soft_exponential.svg/180px-Activation_soft_exponential.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Activation_soft_exponential.svg/240px-Activation_soft_exponential.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mo>−<!-- − --></mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mrow>
                        <mi>ln</mi>
                        <mo>⁡<!-- ⁡ --></mo>
                        <mo stretchy="false">(</mo>
                        <mn>1</mn>
                        <mo>−<!-- − --></mo>
                        <mi>α<!-- α --></mi>
                        <mo stretchy="false">(</mo>
                        <mi>x</mi>
                        <mo>+</mo>
                        <mi>α<!-- α --></mi>
                        <mo stretchy="false">)</mo>
                        <mo stretchy="false">)</mo>
                      </mrow>
                      <mi>α<!-- α --></mi>
                    </mfrac>
                  </mrow>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mi>x</mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo>=</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mrow>
                        <msup>
                          <mi>e</mi>
                          <mrow class="MJX-TeXAtom-ORD">
                            <mi>α<!-- α --></mi>
                            <mi>x</mi>
                          </mrow>
                        </msup>
                        <mo>−<!-- − --></mo>
                        <mn>1</mn>
                      </mrow>
                      <mi>α<!-- α --></mi>
                    </mfrac>
                  </mrow>
                  <mo>+</mo>
                  <mi>α<!-- α --></mi>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo>&gt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}-{\frac {\ln(1-\alpha (x+\alpha ))}{\alpha }}&amp;{\mbox{for}}&amp;\alpha &lt;0\\x&amp;{\mbox{for}}&amp;\alpha =0\\{\frac {e^{\alpha x}-1}{\alpha }}+\alpha &amp;{\mbox{for}}&amp;\alpha &gt;0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/22b03b2a67dddb51c1ecfdb1a8bbecdcabd3eed4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -5.005ex; width:39.278ex; height:11.176ex;" alt="{\displaystyle f(\alpha ,x)=\left\{{\begin{array}{rcl}-{\frac {\ln(1-\alpha (x+\alpha ))}{\alpha }}&amp;{\mbox{for}}&amp;\alpha <0\\x&amp;{\mbox{for}}&amp;\alpha =0\\{\frac {e^{\alpha x}-1}{\alpha }}+\alpha &amp;{\mbox{for}}&amp;\alpha >0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mo>,</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mn>1</mn>
                      <mrow>
                        <mn>1</mn>
                        <mo>−<!-- − --></mo>
                        <mi>α<!-- α --></mi>
                        <mo stretchy="false">(</mo>
                        <mi>α<!-- α --></mi>
                        <mo>+</mo>
                        <mi>x</mi>
                        <mo stretchy="false">)</mo>
                      </mrow>
                    </mfrac>
                  </mrow>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo>&lt;</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <msup>
                    <mi>e</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mi>α<!-- α --></mi>
                      <mi>x</mi>
                    </mrow>
                  </msup>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>α<!-- α --></mi>
                  <mo>≥<!-- ≥ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}{\frac {1}{1-\alpha (\alpha +x)}}&amp;{\mbox{for}}&amp;\alpha &lt;0\\e^{\alpha x}&amp;{\mbox{for}}&amp;\alpha \geq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c9e6b9e176cdbccc0ab43b113dbacdfb346d30cc" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:35.32ex; height:7.509ex;" alt="{\displaystyle f'(\alpha ,x)=\left\{{\begin{array}{rcl}{\frac {1}{1-\alpha (\alpha +x)}}&amp;{\mbox{for}}&amp;\alpha <0\\e^{\alpha x}&amp;{\mbox{for}}&amp;\alpha \geq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mo>−<!-- − --></mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo>,</mo>
        <mi mathvariant="normal">∞<!-- ∞ --></mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (-\infty ,\infty )}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8c11c44279888c9e395eeb5f45d121348ae10a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:9.362ex; height:2.843ex;" alt="(-\infty ,\infty )"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
<td style="background: #FED; color: black; vertical-align: middle; text-align: center;" class="depends table-depends">Yes <a href="/wiki/If_and_only_if" title="If and only if">iff</a> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
        <mo>=</mo>
        <mn>0</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha =0}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/30cc00f65bbc630448311dd2dc82e7ce5e90985a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:5.78ex; height:2.176ex;" alt="\alpha =0"></span></td>
</tr>
<tr>
<td><a href="/wiki/Sine_wave" title="Sine wave">Sinusoid</a></td>
<td><a href="/wiki/File:Activation_sinusoid.svg" class="image"><img alt="Activation sinusoid.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Activation_sinusoid.svg/120px-Activation_sinusoid.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Activation_sinusoid.svg/180px-Activation_sinusoid.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Activation_sinusoid.svg/240px-Activation_sinusoid.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>sin</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\sin(x)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/5fb1266b7f7718442e31e45eef3d81bef6a8b9af" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:13.626ex; height:2.843ex;" alt="f(x)=\sin(x)"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>cos</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=\cos(x)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8cba0d31b2482c08dda6ec9adfd04fa7e3d9372f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:14.615ex; height:3.009ex;" alt="{\displaystyle f'(x)=\cos(x)}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">]</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [-1,1]}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/51e3b7f14a6f70e614728c583409a0b9a8b9de01" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:6.523ex; height:2.843ex;" alt="[-1,1]"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#9F9;vertical-align:middle;text-align:center;" class="table-yes">Yes</td>
</tr>
<tr>
<td><a href="/wiki/Sinc_function" title="Sinc function">Sinc</a></td>
<td><a href="/wiki/File:Activation_sinc.svg" class="image"><img alt="Activation sinc.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Activation_sinc.svg/120px-Activation_sinc.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Activation_sinc.svg/180px-Activation_sinc.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Activation_sinc.svg/240px-Activation_sinc.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>=</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mrow>
                        <mi>sin</mi>
                        <mo>⁡<!-- ⁡ --></mo>
                        <mo stretchy="false">(</mo>
                        <mi>x</mi>
                        <mo stretchy="false">)</mo>
                      </mrow>
                      <mi>x</mi>
                    </mfrac>
                  </mrow>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≠<!-- ≠ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=\left\{{\begin{array}{rcl}1&amp;{\mbox{for}}&amp;x=0\\{\frac {\sin(x)}{x}}&amp;{\mbox{for}}&amp;x\neq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3e8b474cc1b4f1fae11f44d00481ec332e5c00de" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:28.407ex; height:7.509ex;" alt="{\displaystyle f(x)=\left\{{\begin{array}{rcl}1&amp;{\mbox{for}}&amp;x=0\\{\frac {\sin(x)}{x}}&amp;{\mbox{for}}&amp;x\neq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mrow>
          <mo>{</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mtable columnalign="right center left" rowspacing="4pt" columnspacing="1em">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>=</mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mrow>
                        <mi>cos</mi>
                        <mo>⁡<!-- ⁡ --></mo>
                        <mo stretchy="false">(</mo>
                        <mi>x</mi>
                        <mo stretchy="false">)</mo>
                      </mrow>
                      <mi>x</mi>
                    </mfrac>
                  </mrow>
                  <mo>−<!-- − --></mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mrow>
                        <mi>sin</mi>
                        <mo>⁡<!-- ⁡ --></mo>
                        <mo stretchy="false">(</mo>
                        <mi>x</mi>
                        <mo stretchy="false">)</mo>
                      </mrow>
                      <msup>
                        <mi>x</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msup>
                    </mfrac>
                  </mrow>
                </mtd>
                <mtd>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mtext>for</mtext>
                  </mrow>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>≠<!-- ≠ --></mo>
                  <mn>0</mn>
                </mtd>
              </mtr>
            </mtable>
          </mrow>
          <mo fence="true" stretchy="true"></mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x=0\\{\frac {\cos(x)}{x}}-{\frac {\sin(x)}{x^{2}}}&amp;{\mbox{for}}&amp;x\neq 0\end{array}}\right.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/56e5cced47ff630c9319bd26793a2cf368496087" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.04ex; margin-bottom: -0.298ex; width:37.292ex; height:7.843ex;" alt="{\displaystyle f'(x)=\left\{{\begin{array}{rcl}0&amp;{\mbox{for}}&amp;x=0\\{\frac {\cos(x)}{x}}-{\frac {\sin(x)}{x^{2}}}&amp;{\mbox{for}}&amp;x\neq 0\end{array}}\right.}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">[</mo>
        <mo>≈<!-- ≈ --></mo>
        <mo>−<!-- − --></mo>
        <mn>.217234</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">]</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle [\approx -.217234,1]}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7813b154f09cf5aa32f9fa13dc519fd85b1df60a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:15.509ex; height:2.843ex;" alt="{\displaystyle [\approx -.217234,1]}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
<tr>
<td><a href="/wiki/Gaussian_function" title="Gaussian function">Gaussian</a></td>
<td><a href="/wiki/File:Activation_gaussian.svg" class="image"><img alt="Activation gaussian.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_gaussian.svg/120px-Activation_gaussian.svg.png" width="120" height="60" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_gaussian.svg/180px-Activation_gaussian.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Activation_gaussian.svg/240px-Activation_gaussian.svg.png 2x" data-file-width="120" data-file-height="60"></a></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>f</mi>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <msup>
          <mi>e</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <msup>
              <mi>x</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msup>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f(x)=e^{-x^{2}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1bed0b77b34cab03996deb42d464becab2f05636" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:11.966ex; height:3.509ex;" alt="{\displaystyle f(x)=e^{-x^{2}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>f</mi>
          <mo>′</mo>
        </msup>
        <mo stretchy="false">(</mo>
        <mi>x</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mo>−<!-- − --></mo>
        <mn>2</mn>
        <mi>x</mi>
        <msup>
          <mi>e</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>−<!-- − --></mo>
            <msup>
              <mi>x</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msup>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle f'(x)=-2xe^{-x^{2}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/70a7b3d396a5e9e1fc5395a0017733abba868169" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:17.031ex; height:3.509ex;" alt="{\displaystyle f'(x)=-2xe^{-x^{2}}}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo stretchy="false">(</mo>
        <mn>0</mn>
        <mo>,</mo>
        <mn>1</mn>
        <mo stretchy="false">]</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle (0,1]}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7e70f9c241f9faa8e9fdda2e8b238e288807d7a4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:4.963ex; height:2.843ex;" alt="{\displaystyle (0,1]}"></span></td>
<td><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>C</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi mathvariant="normal">∞<!-- ∞ --></mi>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle C^{\infty }}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/971ed05871d69309df32efdfd2020128c9cf69d8" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:3.691ex; height:2.343ex;" alt="C^{\infty }"></span></td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
<td style="background:#F99;vertical-align:middle;text-align:center;" class="table-no">No</td>
</tr>
</tbody><tfoot></tfoot></table>














Idea "forced neural networks" for faster learning.

Make networks learn faster by setting



How deep should a network be?
Question how many features do you think exists in the data you are trying to predict?









Make a much more shallow network.

Search gradient loss in each additional layer of the network.


http://cs231n.github.io/neural-networks-1/
