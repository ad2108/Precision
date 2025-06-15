# Simple tools to better the precision of simple calculations

## Use of Integers instead of Floats

### Concept

To get a better precision in calculations it is possible to use integers instead of floats. Higher precision is achieved, because integers in python 3 are only limited by available memory. Floats on the other hand are limited in python to 64-bit numbers. Using integers instead of floats therefore yields more precise results.

To convert a number from float to a integer, without losses the float is multiplied with $10^{factor}$ and the factor passed with the resulting integer. The resulting pattern is:

$$n_{float} = (n_{int}, fac_{int})$$

In this function $n_{int}$ equals to $n_{float} \cdot 10^{fac_{int}}$. To retrieve the float from the integer and factor the following formula can be applied:

$$n_{float} = n_{int} \cdot 10^{-fac_{int}}$$

### Implemented functions

#### Import

To import the functions use the following code:

```python
import precision_advancer_int as pai
```

#### to_int

This function converts a number to a tuple that contains $n_{int}$ and $fac_{int}$. For input eather floats (Attention!!! Numbers limited to 64-bit) or as strings.

```python
# convert 1.2 to (12, -1)
pai.to_int(1.2)

# convert 1000000.000002 to (1000000000002, -6)
pai.to_int('1000000.000002')
``` 

#### from_int

This function converts the tuple notation back to a float

```python
# convert (12, -1) to 1.2
pai.from_int((12, -1))
``` 

#### dec_to_int

This function is a decorator that can be used to convert the result of a function to the tuple notation. It can only convert a single value!

```python
#a function using the dec_to_int function
@pai.dec_to_int
def add(x, y):
  return x+y

add(1, 2) # returns (3, 0)
```

#### dec_from_int

This function is a decorator that can be used to convert the result of a function from the tuple notation to a float. It can only convert a single value! It is used like the dec_to_int decorator.

#### add

This functions can add up numbers in the tuple notation.

```python
# adding numbers in the tuple notation
pai.add((12, -3), (13, -2)) # returns (142, -3)
```

#### sub, mul, div

The functions sub, mul and div work like the add function. The function sub subtracts all following numbers from the first number and the function div divides the first number by all following numbers.

