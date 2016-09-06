#coding:utf-8
#!/bin/python

def func(coeff):
    sum = ''
    for key in coeff:
        sum = sum + '+' + str(key) + '*' + 'x' + '**' + str(coeff[key])
    return sum[1:]


from sympy import *
from sympy.core.sympify import SympifyError

expr = func({2: 0, 3: 1, 4: 2, 5: 7})
print "expr:", expr
x = Symbol("x")
sexpr = sympify(expr)
print "sexpr", sexpr
print diff(sexpr, x)
print diff(sexpr, x).subs('x', 3)

#(2+3*x+4*x**2+7*x**3.7).diff(x).subs({x:3}).evalf()