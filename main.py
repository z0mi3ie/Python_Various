# Kyle Vickers
# Homework 5
# Python Functions
# CS671

import string
import collections
import sets
import operator
from string import maketrans
from decimal import *


def filter(f, lst):
    ''' Return a filtered list of the given boolean function '''
    out_list = []
    for c in lst:
        if f(c):
            out_list = out_list + [c]
    return out_list


def matchBrackets(s):
    ''' Determines if brackets are correctly matched.
    Uses a stack based algorithm adding all right
    opened brackets to the stack and check then
    pop all left opened brackets that occur. If
    the last bracket added does not match the new
    closing bracket found this returns false.
    Also returns false if by the end of the function
    we still have elements in the bracket stack.
    '''
    all_bracks = []
    for c in list(s):
        if c == "(" or c == '{' or c == '[' or c == '<':
            all_bracks += c
        if c == '}' and all_bracks.pop(-1) != '{':
            return False
        if c == "]" and all_bracks.pop(-1) != "[":
            return False
        if c == ">" and all_bracks.pop(-1) != "<":
            return False
        if c == ")" and all_bracks.pop(-1) != "(":
            return False
    return len(all_bracks) == 0


def wordCounts(s):
    ''' Returns list of words and their counts
    This function returns a list of tuples, each
    having its own unique word from the string and
    the number of times that word occurred in the
    string. The list is ordered from greatest # of
    occurrences to the least number of occurrences
    '''
    split_list = s.lower().split()
    stripped_list = []
    for x in split_list:
        stripped_list.append(x.strip(string.punctuation))
    count_dict = collections.Counter(stripped_list)
    unique_list = list(sets.Set(stripped_list))
    ret_list = []
    for x in unique_list:
        ret_list.append((x, count_dict[x]))
    ret_list.sort(key=lambda x: x[1])
    list.reverse(ret_list)
    return ret_list


def isPrime(n):
    ''' True if n is prime
    Checks odd numbers 3 through the square root of n
    to see if they have a modulos of 0. If they do then
    they can not be prime and returns False
    '''
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    # Check even bit :)
    if not 00000001 & n:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def nthPrime(n):
    ''' Returns the nth prime number.
    This function uses memoization and the helper
    function is prime to return the nth prime number
    asked for.
    '''
    if nthPrime.primes != None:
        pass
    else:
        nthPrime.primes = [1]
    nth_count = len(nthPrime.primes) - 1
    nth_prime = nthPrime.primes[-1]
    x = nth_prime
    if(n <= nth_count):
        return nthPrime.primes[n]
    while(nth_count < n):
        if isPrime(x) and x != nthPrime.primes[-1]:
            nthPrime.primes += [x]
            nth_prime = x
            nth_count += 1
            x += 1
        else:
            x += 1
    return nthPrime.primes[-1]
nthPrime.primes = None


class USDollar:

    ''' A class representing a USDollar
    By using arithmetic functionality, rounding, and
    properties this class is a full representation
    of a USDollar.
    '''

    def __init__(self, value):
        getcontext().rounding = ROUND_FLOOR
        self._value = float(Decimal(value).quantize(Decimal('.01')))

    def __repr__(self):
        return "${0:.2f}".format(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def apply(self, f, value):
        if isinstance(value, int):
            return f(self._value, value)
        if isinstance(value, float):
            return f(self._value, USDollar.formatValue(self, value))
        if isinstance(value, USDollar):
            return f(self._value, value._value)
        raise TypeError("Invalid type passed to USDollar")

    def doArithmetic(self, f, value):
        return apply(self, f, value)

    def formatValue(self, x):
        return float(Decimal(x).quantize(Decimal('.01')))

    def __eq__(self, value):
        return USDollar.apply(self, operator.__eq__, value)

    def __lt__(self, value):
        return USDollar.apply(self, operator.__lt__, value)

    def __le__(self, value):
        return USDollar.apply(self, operator.__le__, value)

    def __ge__(self, value):
        return USDollar.apply(self, operator.__ge__, value)

    def __gt__(self, value):
        return USDollar.apply(self, operator.__gt__, value)

    def applyArith(self, f, value):
        if isinstance(value, int):
            return USDollar(f(self._value, value))
        if isinstance(value, float):
            return USDollar(f(self._value, USDollar.formatValue(self, value) ) )
        if isinstance(value, USDollar):
            return USDollar(f(self._value, value._value))
        raise TypeError("Invalid type passed to USDollar")

    def __add__(self, value):
        return USDollar.applyArith(self, operator.__add__, value)

    def __sub__(self, value):
        return USDollar.applyArith(self, operator.__sub__, value)

    def __iadd__(self, value):
        if isinstance(value, float):
            self._value += USDollar.formatValue(self, value)
            return self
        if isinstance(value, int):
            self._value += value
            return self
        if isinstance(value, USDollar):
            self._value += value._value
            return self
        else:
            raise TypeError("Invalid type passed to USDollar")

    def __isub__(self, value):
        if isinstance(value, float):
            self._value -= USDollar.formatValue(self, value)
            return self
        if isinstance(value, int):
            self._value -= value
            return self
        if isinstance(value, USDollar):
            self._value -= value._value
            return self
        else:
            raise TypeError("Invalid type passed to USDollar")
