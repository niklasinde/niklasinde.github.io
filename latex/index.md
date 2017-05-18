# How to write latex:
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>

First go to [sharelatex.com](sharelatex.com). Create an account and start doing yo thang.

Nice simple snippets.<br/>

## Index

1. [\today](#today)
2. [something](#something)
3. [something](#something)





### <a name="today"></a>\today
Set title to:
```latex
\title{\today}
```
So if you'r working on a project for a long time you don't have to update the date everyday.


### <a name="code"></a>code
```latex
\begin{lstlisting}[language = R]
[1] "mean error test:" "1.46934685949842"
[1] "mean error train:" "2.38344678143766"
[1] "mean error test:" "1.44979433585936"
[1] "mean error train:" "2.47167748969558"
\end{lstlisting}
```
Really nice way to include code in you latex document

### <a name="img"></a>Include images
```latex
\begin{figure}[H]
\centering
\title{}
\includegraphics[scale= 0.5]{filename}
\end{figure}
```
Conditional function
```
\[
    X=
\begin{cases}
    1,& \text{if male} \\
    0,              & \text{if women}
\end{cases}
\]
```
Tabels
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
