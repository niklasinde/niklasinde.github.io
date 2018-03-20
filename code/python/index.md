# Python
[Pycharm settings and short commands](pycharm/)


[How to structure your project](structure/)

## Import statements

There are two ways to import stuff into python:
```python
 from module import function/Classes as name
 ```
and
```python
import module
```

Note that

```python
import module
```
and
```python
 from module import * as module
```
 is the same thing.

## snippets
### for loops and list comprehension
```python
l = []
for i in range(10):
  l.append(i)

l == [i for i in range(10)]
>>>True
```
### for dicts

```python
d = {4: 10, 10: 9, 2: 8}
for index, key in enumerate(d):
  print(index, key)

>>>0 4
>>>1 10
>>>2 2

```
or
```python
for key, value in d.items():
  print(key, value)

>>>4 10
>>>10 9
>>>2 8

```

# Different type of structures.
## Lists
###Find index

```python
l = [1,2,"hej",4,5]

l.index("hej")
>>> 2
```


# Classes
## Basics
Classes are stuff unlike function used when you have functions that you wish to save data in.

In classes an important thing is the self thingy

For example if we do:

```python
class Example:
  def __init__(self, values)
    self.values


ex = Example(2)
print(ex.values)
>>> 2
```

## Builtin functions
```python
class Example:

```

### init__
The function that is called then the class in instantiated.


### __getitem__(key)
The function that is called when Example[key].

### __setitem__(key, value)
The function that is called when Example[key] = value.

### __call__()
The function that is called when Example()

## Property

Property is used when you have a variable




### np.arrays


### pd.
