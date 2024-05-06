

# How to write latex:


First go to [sharelatex.com](sharelatex.com). Create an account and start doing yo thang.<br/>
### Do not download the thing to your computer. Nightmare.
### Quick mathjax syntax for markdown.
Inside text
```markdown
$$
```
Free centerpiece
```markdown
$$
```
Nice simple snippets.<br/>

## Index

1. [General functions](#general)
2. [\something](#matrix)
3. [something](#conditional)

## No indent

```latex
\noindent
```
or
```latex
\setlength\parindent{0pt}
```
<a name="today">Today</a>
Set title to:
```latex
\title{\today}
```
So if you'r working on a project for a long time you don't have to update the date everyday.


## legend
```r
legend(c("bottomright"),legend=c("Group1","Group2","Group3"),lwd=c(2.5,2.5),col=c("red","green","blue"))
```
## Distribution sign in latex
$X \sim N(\mu,\sigma^2)$
```latex
\sim
```

<a name"matrix">Matrix</a>

```latex
\left[\begin{array}[ccc]
  0 & 1 & 2 \\
  3 & 4 & 5 \\
  6 & 7 & 8
\end{array}\right]
```
$$
\left[\begin{array}[cc]\\
  2 & 2 \\
  3 & 4\\
  6 & 7
\end{array}\right]
$$

$\frac{1}{2}$
### Code <a name="code"></a>code

```latex
\begin{lstlisting}[language = R]
[1] "mean error test:" "1.46934685949842"
[1] "mean error train:" "2.38344678143766"
[1] "mean error test:" "1.44979433585936"
[1] "mean error train:" "2.47167748969558"
\end{lstlisting}
```
Really nice way to include code in you latex document

### <a name="img">Include images</a>
```latex
\begin{figure}[H]
\centering
\title{}
\includegraphics[scale= 0.5]{filename}
\end{figure}
```
Conditional function
```latex
    X=
\begin{cases}
    1,& \text{if happy} \\
    0,& \text{if super happy}
\end{cases}
```
$$
    X=
\begin{cases}
    1,& \text{if happy} \\
    0,              & \text{if super happy}
\end{cases}
$$



### Tabels
```latex
\begin{table}[H]
\centering
\caption{My caption}
\label{my-label}
\begin{tabular}{lll}
  & 0  & 1  \\
0 & 40 & 10 \\
1 & 12 & 18
\end{tabular}
\end{table}
```
Note: change the number of "l" to the number of columns in your table.
$$\begin{table}[H]
\centering
\caption{My caption}
\label{my-label}
\begin{tabular}{lll}
0  & 0  & 1  \\
0 & 40 & 10 \\
1 & 12 & 18
\end{tabular}
\end{table}$$


### Arrows

$\leftarrow \rightarrow \leftrightarrow$
```latex
\rightarrow
\leftarrow
\leftrightarrow
```
