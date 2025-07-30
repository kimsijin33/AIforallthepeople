#!/bin/bash

#250727 p63
>>> from sympy import expand, factor, Symbol
>>> x = Symbol('x')
>>> expand((x + 1) * (x +5))
x**2 + 6*x + 5
>>> factor(x**2 + 6*x + 5)
(x + 1)*(x + 5)

#250728 p75
>>> import math
>>> pow = math.pow(2, 5)
>>> print("pow 결과" ".format(pow))
  File "<stdin>", line 1
    print("pow 결과" ".format(pow))
                                 ^
SyntaxError: EOL while scanning string literal
>>> print("pow 결과: {}".format(pow))
pow 결과: 32.0
>>> sqrt = math.sqrt(2)
>>> print(f"sqrt 결과: {sqrt}")
sqrt 결과: 1.4142135623730951
>>> exp = math.exp(2)
>>> print(f"exp 결과: {exp}")
exp 결과: 7.38905609893065

#250729 p83
import math
math.log(2,4)

math.log(4,2)


#250731
import math
from sympy import expand, Symbol
x = Symbol('x')
a = Symbol('a')
x = 3
expand((a*x)+2) = 8

>>> from sympy import expand, factor, Symbol
>>> x = Symbol('x')
>>> expand((x + 1) * (x +5))


