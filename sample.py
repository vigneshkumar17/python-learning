# Variables and Types

# simple variable declarations
myint=7
print(myint)

myfloat=8.0
print(myfloat)
myfloat=float(11.23)
print(myfloat)

sampleString='hi'
print(sampleString)
sampleString="hello"
print(sampleString)
sampleString="welcome to python"
print(sampleString)

# concat of two variables
# Note: cannot concat two different datatype values
one=1
two=2
three=one+two
print(three)

string1="Hello"
string2="World"
string3=string1+string2
print(string3)
a,b=3,2
print(a,b)

mystring="hello"
myfloat=11.50
myint=12

if isinstance(mystring,str)and mystring=="hello":
    print("string is: %s" %mystring)
else:print("String is not valid")
if isinstance(myfloat,float) and myfloat==11.50:
    print("Float value is %f" %myfloat)
else:print("float is not valid")
if myint==12:
    print(myint)

# Lists

# simple way to add a value in the list and to print
mylist=[]
mylist.append(1)
mylist.append(13)
mylist.append(10035.50)
mylist.append("asda")

for i in mylist:
    print(i)

# assigning three values to a list
mylist=[1,2,3]
# trying to access the 4th index throws exception "IndexError: list index out of range"
print(mylist[3])

# Basic Operators

#Arithmetic Operators
sum=1+2
print(sum)

sub=1-2
print(sub)

operations=2*4-3+1
print(operations)

operations=2*(4-3)+1
print(operations)

#in the below case (5/2) operation occurs first and the addition occurs.
#and (5/2) returns a whole number (2) instead of decimal value
operations=2+5/2
print(operations)

operations= 11%2
print(operations)

#Square and cube operations
oper1=2**2
oper2=2**3
oper3=2**4
print(oper1,oper2,oper3)

#string can be multiplied to display multiple times
oper="hello" *2
print(oper)

#Joinig two list element
num1=[3,5,2,7,8]
num2=[2,7,3,6,1]
num3=num1+num2
print(num3)

#like string, list element can also be displayed multiple times
print([2,4,6]*2)