# Functions for each one of the numbers from 0 to 9

def ZERO(f=None):
    if f is None:
        return 0
    return f(0)

def ONE(f=None):
    if f is None:
        return 1
    return f(1)

def TWO(f=None):
    if f is None:
        return 2
    return f(2)

def THREE(f=None):
    if f is None:
        return 3
    return f(3)

def FOUR(f=None):
    if f is None:
        return 4
    return f(4)

def FIVE(f=None):
    if f is None:
        return 5
    return f(5)

def SIX(f=None):
    if f is None:
        return 6
    return f(6)

def SEVEN(f=None):
    if f is None:
        return 7
    return f(7)

def EIGHT(f=None):
    if f is None:
        return 8
    return f(8)

def NINE(f=None):
    if f is None:
        return 9
    return f(9)

# Functions for the math operations plus, minus, multiplication

def PLUS(x):
    return lambda y: y + x

def MINUS(x):
    return lambda y: y - x

def TIMES(x):
    return lambda y: y * x

# The calculations are made in the following form: NUMBER(OPERATION(NUMBER()))
# NUMBER: ZERO, ΟΝΕ, ..., NINE
# OPERATION: PLUS, MINUS, TIMES
# e.g. SEVEN(TIMES(FIVE())) output: 35
