import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
def add(a, b): 
    return a + b

def sub(a, b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a
def log(a,b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(a, b)
def exp(a,b):
    return a**b




def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError

def exp(a, b):
    return math.pow(a, b)

