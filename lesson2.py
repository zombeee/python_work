#! /usr/bin/env python


"""
Logical operations, functions, namespaces
"""

from __future__ import division, print_function


# Logical operations

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

3 != 4 is True
True and not ("testing" != "test" or "Python" == "Python")
"testing" != "test" is True
True and not (True or "Python" == "Python")
"Python" == "Python"
True and not (True or True)

# identity and equality

1 == True
1 is True

# NoneType

None is False
not None

# Tertiary operator

a = 1
b = a + 1 if a else 1

# and/or evaluation

c = a and b
a = 0
c = a and b
c = a or b


def sqr(number):
    return number**2


q = sqr(2) + sqr(3)

def root(num):
    return num**0.5 if num >= 0 else None


def root(num):
    return num >= 0 and num**0.5 or None


# anti-example
def root(num):
    if num >= 0:
        rt = num**0.5
    else:
        rt = None
    return rt


# anti-example
def root(num):
    if num >= 0:
        return num**0.5
    return None

# Namespaces. 

a = 1


def test1():
    print(a)


def test2():
    a = 2
    print(a)


def test3(a):
    print(a)
    a = 2


def test4():
    print(a)
    a = 2

# What will be printed to the console each time?

test1()
test2()
test2(a)
test3()
test3(a)
test4(a)
test4()


