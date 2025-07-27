#!/bin/bash

#250727 p63
>>> from sympy import expand, factor, Symbol
>>> x = Symbol('x')
>>> expand((x + 1) * (x +5))
x**2 + 6*x + 5
>>> factor(x**2 + 6*x + 5)
(x + 1)*(x + 5)



