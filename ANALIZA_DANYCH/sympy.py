# -*- coding: utf-8 -*-

# -- Sheet --

import sympy

sympy.init_printing()

from sympy import I,pi,oo

x = sympy.Symbol("x")
print(x)

y = sympy.Symbol("y",real=True)
print(y.is_real)

z = sympy.Symbol("z",imaginery=True)
print(z.is_real)

sympy.sqrt(x**2)

n1,n2,n3 = sympy.Symbol("n"),sympy.Symbol("n",integer=True),sympy.Symbol("n",odd=True)

sympy.cos(n1*pi)

sympy.cos(n2*pi)

sympy.cos(n3*pi)

i = sympy.Integer(19)

f"i={i} [typ:{type(i)}]"

f = sympy.Float(2.37)

f"f={f} [typ:{type(f)}]"

f.is_Integer, f.is_real, f.is_odd

n= sympy.Symbol("n",integer=True)

n.is_integer, n.is_Integer, n.is_positive, n.is_Symbol

i = sympy.Integer(19)

i.is_integer, i.is_Integer, i.is_positive, i.is_Symbol

i**150

print(sympy.factorial(100000))

# Liczy wymierne w bibliotece **SymbolicPython**


sympy.Rational(11,13)

r1 = sympy.Rational(2,3)
r2 = sympy.Rational(4,5)

r1*r2

r1/r2

r1-r2

# Definicje funkcji w bibliotece **sympy**


x,y,z = sympy.symbols("x,y,z")

f = sympy.Function("f")

type(f)

f(x)

g = sympy.Function("g")(x,y,z)
g

sympy.sin

sympy.sin(x)

sympy.sin(pi*1.5)

h = sympy.Lambda(x,x**2)
h

h(5)

h(1+x)

# wyrażenia w **sympy**


x = sympy.Symbol("x")

e = 1+2*x**2+3*x**3
e

e.args

e.args[1].args[1]

expr = 2*(x**2-x)-x*(x+1)
expr

sympy.simplify(expr)

exprtryg = 2*sympy.cos(x)*sympy.sin(x)
exprtryg

sympy.trigsimp(exprtryg)

expre = sympy.exp(x)*sympy.exp(y)
expre

sympy.powsimp(expre)

expr = (x+1)*(x+2)
expr

sympy.expand(expr)

sympy.sin(x+y).expand(trig=True)

a,b = sympy.symbols("a,b",positive=True)

sympy.exp(I*a+b).expand(complex=True)

sympy.exp(I*(a-b)*x).expand(power_exp=True)

# FAKTORYZCJA


sympy.factor(x**2-1)

sympy.factor(x*sympy.cos(y)+sympy.sin(z)*x)

sympy.logcombine(sympy.log(a)-sympy.log(b))

expr = x+y+x*y*z

expr.factor()

expr.collect(x)

expr.collect(y)

expr = sympy.cos(x+y)+sympy.sin(x-y)
expr

expr.expand(trig=True).collect([sympy.cos(x),sympy.sin(x)]).collect(sympy.cos(y)-sympy.sin(y))

sympy.apart(1/(x**2+3*x+2),x)

sympy.together(1/(y*x+y)+1/(1+x))

sympy.cancel(y/(y*x+y))

(x+y).subs(x,y)

sympy.sin(x*sympy.exp(x)).subs(x,y)

expr = x*y+z**2*x
expr

values = {x:1.25, y:0.4,z:3.2}

expr.subs(values)

# rachanek różniczkowy w **sympy**


f = sympy.Function('f')(x)

sympy.diff(f,x)

sympy.diff(f,x,x)

g = sympy.Function('g')(x,y)

g.diff(x,y)

expr = x**4+x**3+x**2+x+1
expr

expr.diff(x)

expr = sympy.sin(x*y)*sympy.cos(x/2)
expr

expr.diff(x)

expr = sympy.functions.special.polynomials.hermite(x,0)
expr

expr.diff(x).doit()

