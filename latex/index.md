# How to write latex:


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
Really nice way to include code in you \latex document

### <a name="img"></a>Include images
```latex
\begin{figure}[H]
\centering
\title{}
\includegraphics[scale= 0.5]{filename}
\end{figure}
```
