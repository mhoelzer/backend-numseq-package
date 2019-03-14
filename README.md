<p align="center">
  <img src=logo.jpg/>
</p>

# Kenzie Academy: Numseq Package

## Assignment Objective

Explore and understand how to create your own modules and packages

## Overview

In this assignment you will create several modules for computing various numeric sequences. The modules will then be grouped into a hierarchical package structure. Your test function will import modules from within your numseq package, and test their functionality.

Begin by creating a package named **numseq**.

## Fibonacci numbers

Within the numseq package, create a module named fib. Within the fib module, define a function fib(n) that returns the nthFibonacci number.

### Test Code

```
from numseq.fib import fib

print ("Fibonacci")
for i in range(10):
    print ("{}: {}".format(i, fib(i)))
```

### Expected Output

```
Fibonacci
0: 0
1: 1
2: 1
3: 2
4: 3
5: 5
6: 8
7: 13
8: 21
9: 34
```

## Geometric numbers

Within the numseq package, create a module named geo. Within the geo module, define 3 functions:

- square(n)\
  ![Square-Numbers-1.png](https://my.kenzie.academy/courses/34/files/2618/preview?verifier=VriaFLlyiAl8ppB3GZKv30iQkzBR5BqR8qMdhzdE)

- triangle(n)\
  ![First_six_triangular_numbers.png](https://my.kenzie.academy/courses/34/files/2622/preview?verifier=yGWyLtLptASmXBGH2dq4YqRTyFPynIQ7EO0phR3x)

- cube(n)\
  ![cube_numbers.gif](https://my.kenzie.academy/courses/34/files/2629/preview?verifier=VrQpYjGtFRNDLCg54hCjbLd97s791I43OyAx3A4I)

### Test Code

```
from numseq.geo import *

print("Geometric numbers (square, triangle, cube)")
for i in range(10):
 print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))
```

### Expected Output

```
Geometric numbers (square, triangle, cube)
0: 0 0 0
1: 1 1 1
2: 4 3 8
3: 9 6 27
4: 16 10 64
5: 25 15 125
6: 36 21 216
7: 49 28 343
8: 64 36 512
9: 81 45 729
```

## Prime numbers

Finally, create a module named prime within the numseq package. Define the following functions:

- primes(n) returns a list of all primes less than n
- is_prime(m) returns a boolean indicating whether m is a prime number

### Test Code

```
from numseq.prime import *

print ("Primes")
prime_list = primes(1000)
for p in prime_list[-10:]:
 print (p)
print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))
```

### Expected Output

```
Primes
937
941
947
953
967
971
977
983
991
997
Is 999981 prime? False
Is 999983 prime? True
```

# HAVE FUN :)
