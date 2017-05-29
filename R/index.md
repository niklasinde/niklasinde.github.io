


### Rcode snippets






### <a name="Legend"></a>Add legend in plot
```R
legend("right", legend = c("Total","Sensitivity","Specificity"),
        col=c("black","blue","red"), pch=16)
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
