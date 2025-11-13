import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError

def exp(a, b):
    return math.pow(a, b)

