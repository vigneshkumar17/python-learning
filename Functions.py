# FUNCTIONS

#You invoke a function by writing the function name followed by a tuple of function arguments, such as a = add(3,4).
def test(x,y):
    return x+y

a=test(2,3)
print(a)

def test1():
    b=a+2
    print(b)
test1()

#default value assigned doesn't change

a=10
def sample(x=a):
    print(x)

a=5
sample()

# Assigning a mutable object as default value, leads to unintended behaviour

def sample(x, items=[]):
    items.append(x)
    print(items)
sample(1)
sample(2)
sample(3)
sample(4)
sample(5)
sample(10)

#this default argument retains modification based on previous invocations, so correct way is to assign it as none and add the items later
def sample(x, items=None):
    if items is None:
        items=[]
    items.append(x)
    print(items)

sample(1)
sample(3)
sample(10)


# A function can accept a variable number of parameters if an asterisk (*) is added to the last parameter name:

def sample1(file,fmt,*args):
    file.write(fmt %args)
    sample1.__get__(42,"hello",3.14)
    print sample1()


def one_good_turn(n):
    return n + 1


def deserves_another(m):
    return one_good_turn(m) + 2


a=deserves_another(4)
print(a)


