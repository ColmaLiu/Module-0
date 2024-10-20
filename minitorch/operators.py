"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    return x * y


def id(x: float) -> float:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> float:
    return 1 if x < y else 0


def eq(x: float, y: float) -> float:
    return 1 if x == y else 0


def max(x: float, y: float) -> float:
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    return 1 if abs(x - y) < 0.2 else 0


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))


def relu(x: float) -> float:
    return x if x > 0 else 0


EPS = 1e-6


def log(x: float) -> float:
    return math.log(x + EPS)


def exp(x: float) -> float:
    return math.exp(x)


def log_back(x: float, d: float) -> float:
    return d / (x + EPS)


def inv(x: float) -> float:
    return 1 / x


def inv_back(x: float, d: float) -> float:
    return - d / (x * x)


def relu_back(x: float, d: float) -> float:
    return d if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    def mapFn(iterable: Iterable[float]) -> Iterable[float]:
        return [fn(x) for x in iterable]
    return mapFn


def zipWith(fn: Callable[[float, float], float]) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    def zipWithFn(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
        return (fn(x, y) for x, y in zip(ls1, ls2))
    return zipWithFn


def reduce(fn: Callable[[float, float], float], start: float) -> Callable[[Iterable[float]], float]:
    def reduceFn(ls: Iterable[float]) -> float:
        r = start
        for x in ls:
            r = fn(x, r)
        return r
    return reduceFn


def negList(ls: Iterable[float]) -> Iterable[float]:
    return map(neg)(ls)


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return zipWith(add)(ls1, ls2)

def sum(ls: Iterable[float]) -> float:
    return reduce(add, 0)(ls)


def prod(ls: Iterable[float]) -> float:
    return reduce(mul, 1)(ls)
