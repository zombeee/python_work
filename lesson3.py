#! /usr/bin/env python


"""

Functions, functions,functions

"""



from __future__ import division, print_function


def _and(left, right):
    if bool(left):
        return right
    return left


def _or(left, right):
    if bool(left):
        return left
    return right


def _3op(cond, var1, var2):
    if bool(cond):
        return var1
    return var2

def root(power, num):
    return None if power%2 and num < 0 else num**(1/power)


def _not(val):
    if val:
        return False
    return True


# anti-example

def root(num):
    return (num >= 0 and (lambda: num**0.5) or (lambda: None))()

