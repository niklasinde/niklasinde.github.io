# Different functions in the tensorflow package
´´´python
import tensorflow as tf
´´´


## How to set up a tensorflow code.


Because tensorflow is mostly written in C++ for an increase of speed and for the addvatage that C++ is "closer" to the hardward we have to think of tensorflow code a bit different.<br></br>
Learn by doing:

Start with the input and output variables x and y:

```python
x = tf.Placeholders(dtype=float, shape=[how_many_samples = ?,shape_of_output=200])
y = tf.Placeholder(dtype=float, shape=[how_many_samples = ?,shape_of_output=10])
```
In tensorflow we define all the variables goes backend and displace the results.

If we think of an ordinairy function in python we have:
```python

```



## random_normal
Returns an array with N(0,1)(as standard) distributed array.
```python
random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
    Outputs random values from a normal distribution.

    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
      mean: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
        distribution.
      stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
        of the normal distribution.
      dtype: The type of the output.
      seed: A Python integer. Used to create a random seed for the distribution.
        See
        [`set_random_seed`](../../api_docs/python/constant_op.md#set_random_seed)
        for behavior.
      name: A name for the operation (optional).

    Returns:
      A tensor of the specified shape filled with random normal values.
```
