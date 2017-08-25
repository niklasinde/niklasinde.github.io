

# How to write latex:


First go to [sharelatex.com](sharelatex.com). Create an account and start doing yo thang.<br/>
### Do not download the thing to your computer. Nightmare.
### Quick mathjax syntax for markdown.
Inside text
```markdown
$$
```
Free center piece
```markdown
$$
```
Nice simple snippets.<br/>

## Index

1. [\today](#today)
2. [something](#something)
3. [something](#something)

## No indent

```latex
\noindent
```
or
```latex
\setlength\parindent{0pt}
```
## legend
```r
legend(c("bottomright"),legend=c("Group1","Group2","Group3"),lwd=c(2.5,2.5),col=c("red","green","blue"))
```
## Distribution sign in latex
```latex
\sim
```
## Today <a name="today"></a>
Set title to:
```latex
\title{\today}
```
So if you'r working on a project for a long time you don't have to update the date everyday.

### Matrix <a name"matrix"></a>

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

### <a name="img">netInclude images</a>
```latex
\begin{figure}[H]
\centering
\title{}
\includegraphics[scale= 0.5]{filename}
\end{figure}
```
Conditional function
```latex
\[
    X=
\begin{cases}
    1,& \text{if male} \\
    0,              & \text{if women}
\end{cases}
\]
```
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



### Arrows $leftarrow \rightarrow$
```latex
\rightarrow
\leftarrow
```
