#! /usr/bin/env python

"""

Dictionaries, function arguments and multiple output, objects, state, methods,
iteration, namespaces part 2

"""


from __future__ import division, print_function
import operator
# import operator as op
# from operator import mul
# from operator import mul as multiply
import functools


# Dictionaries


# initialise an empty dictionary
empty_dict = {}  # equivalently `empty_dict = dict()`

# initialise a nonempty dictionary
nonempty_dict = {"key1": "value1", "key2": "value2"}
nonempty_dict_alternative_init = dict(key1="value1", key2="value2")

# subscript (key-access)
print(nonempty_dict["key1"])

# set new value
nonempty_dict["new_key"] = 1

# reset existing key



# Objects


class BaseObject(object):
    """
    This dummy base-class illustrates how objects provide interfaces
    """

    def __init__(self, test_value):
        """
        Initialise (attributes in) a newly created object of class `BaseObject`.
        Evoked on class call, i.e. `BaseObject()`
        Note: `__init__` doesn't create an object (`self`), hence it returns
              nothing, `__new__` does, but that is well beyond our scope for now
              => `__init__` changes state
        """
        pass

    def __len__(self):
        """
        Defines object's length, i.e. evoked by function `len`
        """
        raise NotImplementedError

    def __nonzero__(self):
        """
        Returns boolean representation, i.e. evoked by function `bool`
        :rtype: bool
        """
        raise NotImplementedError

    __bool__ = __nonzero__

    def __call__(self, *args, **kwargs):
        """
        Makes object callable, i.e. allows to use it as a function
        """
        raise NotImplementedError

    def __iter__(self):
        """
        Defines object's iterations protocol, i.e. by `iter`
        """
        raise NotImplementedError

    def __getitem__(self, item):
        """
        Evoked by the subscript operator (`[]`), e.g. `instance[]`
        """
        raise NotImplementedError

    def __setitem__(self, key, value):
        """
        e.g.
        >>> test_lst = [1, 2, 3]
        >>> test_lst[0] = 4  # this triggers `__setitem__`
        """
        raise NotImplementedError

    def __add__(self, other):
        """
        Along with `__radd__` defines addition, i.e. evoked by `+`
        """
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __repr__(self):
        """
        Along with `__str__` provides string representations
        """
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def test_method(self):
        return self.test_attr

tensor = [[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]],

          [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]],

          [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]]

print(tensor[0][0][0])
# write an equivalent step by step

# Iteration and methods

string = "abc"
iterator = iter(string)
print(next(iterator))


depressive_hello_world = "hello damn world"
for char in depressive_hello_world:  # ~ for char in iter(string)
    print(char)

lst = list(depressive_hello_world)
for element in lst:  # ~ for element in iter(lst)
    print(element)

# string parsing (`split` method)
separator = " "  # ~ delimiter
for word in depressive_hello_world.split(separator):
    print(word)

# note: `" "` is the default delimiter
for word in depressive_hello_world.split():
    print(word)

# join string
hello, damn, world = depressive_hello_world.split()
hello_word = separator.join((hello, world))  # ~ `"".join((hello, world))`

def func(numbers):
    a, b = numbers
    return a + b

def func_unpack((a, b)):
    return a + b

def func_std(a, b):
    return a + b

numbers = (1, 2)
func_unpack(numbers)
func_std(numbers[0], numbers[1])


for num in xrange(2, 10):
    if not num % 2:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# zip

numbers1 = range(10)
numbers2 = range(10, 25)

for item in zip(numbers1, numbers2):
    print(item)

# NOTE! how not to iterate
for i in xrange(min(len(numbers2), len(numbers1))):
    print((numbers1[i], numbers2[i]))

# Namespaces Part 2 (name shadowing)


# example 1 or  "...Special cases aren't special enough to break the rules..."
lst = list("abc")
list = list("abc")
new_lst = list("abc")
new_lst = __builtins__.list("abc")
del list
new_lst = list("abs")

# example 2 or "...Namespaces are one honking great idea..."
a = 10
b = 3
if a < b:
    i = 10
print(i)

for i in xrange(10):
    pass

if a < b:
    i = 10
print(i)


# Argument unpacking and multiple returns


# default arguments
def root(number, r=2):  # root(r=2, number) - is an error
    return None if number < 0 and not r % 2 else number**(1/r)

# multiple output
def neighbourhood(num, epsilon):
    return num - epsilon, num + epsilon

lower_bound, upper_bound = neighbourhood(0, 10)


# arbitrary arguments
def show_args(*args, **kwargs):
    print(args)
    print(kwargs)

show_args(1, 2, 3, 2, 3, key=1, key2=1)

print(1, 2, 3, 4, sep=" ", end="\n")

def unpack_args(*args):
    print(*args)

unpack_args(1, 2, 3)

for numbers in zip(xrange(10), xrange(10, 20)):
    print(*numbers)

def unpack_kwargs(**kwargs):
    print(**kwargs)

unpack_kwargs(abs=1, sb=1)

def complete_argument_signature(std_arg, default_arg="value", *args, **kwargs):
    raise NotImplemented


# a quirk
def example1(def_arg=None):
    def_arg = [] if def_arg is None else def_arg
    def_arg.append(1)
    print(def_arg)

# what will be printed to the console?
example1()
example1()


def example2():
    def nested_function(def_arg=[]):
        def_arg.append(1)
        print(def_arg)
    nested_function()

example2()
example2()



def my_min(*args):
    """
    This function find min, in given sequence of simple numbers, or in
    given tuple or in list
    """
    work_args = list(args)
    if len(work_args) == 1:
        for seq in work_args:
            if isinstance(seq, (list, tuple)):
                filtering_seq = list(seq)
                return sorted(filtering_seq)[0]
            else:
                raise ValueError("Can't find min, got only one value")
    else:
        for nums in work_args:
            if isinstance(nums, int):
                return sorted(work_args)[0]
            else:
                raise ValueError("Can't find min, wrong data format")