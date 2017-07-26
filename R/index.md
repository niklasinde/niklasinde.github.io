


### Rcode snippets
# <a name="Legend"></a>Add legend in plot
```R
legend(c("bottomright"),legend=c("Group1","Group2","Group3"),lwd=c(2.5,2.5),col=c("red","green","blue"))
```

### What colors are there?

http://www.stat.columbia.edu/~tzheng/files/Rcolor.pdf

### Sort data frame by some column or row

sorting examples using the mtcars dataset
```R
attach(mtcars)
```

sort by mpg
```R
newdata <- mtcars[order(mpg),]
```
sort by mpg and cyl
```R
newdata <- mtcars[order(mpg, cyl),]
```
sort by mpg (ascending) and cyl (descending)
```R
newdata <- mtcars[order(mpg, -cyl),]

detach(mtcars)
```
