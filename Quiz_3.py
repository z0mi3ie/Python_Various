


'''
Kyle Vickers
Quiz 3 (Python)
CS671
Instr. Sofia Lemons
'''

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1 Data Structures ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Write a function pyMap that emulates SML's map, but does so
using only list comprehensions and can be used on any iterable
data structure. (list, tuple, string, etc)
'''
def pyMap(f, l): return [f(x) for x in l]

pm1 = pyMap( lambda x: x + 1, [1,2,3,4,5] )
pm2 = pyMap( lambda x: x + 1, (1,2,3,4,5) )
pm3 = pyMap( lambda x: x.upper(), "abcdef" )
# print pm1
# print pm2
# print pm3

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2 Variable Scoping ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Write a function printVal that takes a string val as an argument, allowing
it to default to None. It then looks for a variable named val with a value
(that is not None) in the following order of scopes:
    First:  Global
    Second: Function Namespace
    Third:  Paramaters/Local
'''
def printVal(val = None):
    # val = "sup, i'm declared in the function"
    if "val" in globals() != None:
        print "Found val in : globals()", globals()["val"]
    if "val" in printVal.__dict__:
        print "Found val in : Function namespace(example: foo.x) printVal.__dict__", printVal.__dict__["val"]
    if "val" in locals() != None:
        print "Found val in : locals()", locals()["val"]

# val = "hey, im a global"
# printVal.val = "Hey! im in printVal's namespace"    
# printVal("hey, im a parameter")

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#3 Classes & Objects ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Write a class Point2D with x and y values and another class Point3D with
x, y, and z values. Give each class a constructor that takes these
values
'''

### Part A) Basic Point2D and Point3D Classes
class Point2D:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.z = z

class Point3D:
    def __init__(self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z

### Part B) Code filled in for designated subtractions and outputs
class Point2D:
    def __init__(self, x, y, z=0 ):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, them):
        return Point3D(self.x - them.x, self.y - them.y, self.z - them.z) 

class Point3D:
    def __init__(self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, them):
        return Point3D(self.x - them.x, self.y - them.y, self.z - them.z) 

    def __str__(self):
        return "%d, %d, %d" % (self.x, self.y, self.z)

p2d = Point2D(3, 3)
p3d = Point3D(1, 1, 1)
p3d_sub_p3d = p3d - p3d
p2d_sub_p3d = p2d - p3d
p3d_sub_p2d = p3d - p2d


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#4 Metaprogramming ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Part A :: Use metaprogramming to make it so a's string representation 
is in all uppercase, while b's (and all other A objects') are in all 
lowercase.

Part B :: Write a @keepSum decorator that will print a running sum of the
values returned by a function after each call.

Part C :: What will happen to this function if we use the @keepSum
decorator on it? Rewrite it so the decorator will behave more as we
would usually prefer
'''
### Part A 
class A:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

a = A("a's name")
b = A("b's name")
c = A("c's name")
a.__dict__['name'] = a.__dict__['name'].upper()

print a
print b
print c

# print a.__dict__
# print b.__dict__
# print a.__dict__['name'].upper()
# print a
# print b

### Part B
def keepSum(fn, *args):  # fn is the series function. from series, f,n,end are in the args ( which is like varargs, but a list )
    def wrapper(*args):
        ret = fn(*args)
        wrapper.sum += ret
        return ret
    wrapper.sum = 0
    return wrapper

@keepSum
def foo(): return 4

# foo()
# foo()
# foo()

## Part C ###############################################

@keepSum
def series(f, n, end):
    def shits( f, n, end ):
        if n < end: 
            return f(n) + shits(f, n + 1, end)
        else:
            return 0
    return shits(f,n,end)

def oaf(n): return n + 1
series_test = series( oaf, 0, 5 )
series( oaf, 0, 5 )
# print series_test


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#4 Lazy Programming ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Write a function randConverge(mn, mx) that returns a generator object for
integers in range between mn and mx which converges to mn. The integer
generated/returned from the previous step should become the mx for the
next, until mn and mx are the same. So the last integer from the generator
should always be mn, and mn should never be generated twice.

Write a function firstFive(g) that returns a list containing the first 
five items from generator g, placing None in any indeices where the 
generator has run out.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

import random
random.seed()
def randConverge(mn, mx):
    randConverge.max = mx
    randConverge.pre = mx
    while True:
        randConverge.max = random.randint(mn, randConverge.max-1) 
        if mn == randConverge.max:
            yield randConverge.max
            break
        else:
            yield randConverge.max
    while True:
        yield None
randConverge.max  = None

gen1 = randConverge(1, 10)
for x in range( 0, 5 ):
   print next(gen1)

def firstFive(g):
    self.ret = []
    for x in range (0,5):
        self.ret += next(g)

print firstFive( randConverge(1,10) )