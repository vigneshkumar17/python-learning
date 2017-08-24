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

# LIST

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
#print(mylist[3])

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


#creating two list with 10 elements to each list and concatinating two list into one and verifying the count with each list object

x=object()
y=object()

xlist=[x]*10
ylist=[y]*10
z=xlist+ylist

print("value of xlist is %d" %len(xlist))
print("value of ylist is %d" %len(ylist))
print("value of z is %d" %len(z))

if xlist.count(x)==10 and ylist.count(y)==10:
    print("xlist and y list count is valid")
if z.count(x)==10 and z.count(y)==10:
    print("count of z list according to x and y together is valid")

#String formatting
#Python uses C-style string formatting to create new, # formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list).
# together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".


#%s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

name="vicky"
print("hello %s"%name)
age=24
print("%s is %d old"%(name,age))
alist=[1,2,3]
print("list is %s" %alist)

details=("vignesh","kumar",50)
formatstring="hello %s %s. your current balance is $%s"

print(formatstring%details)

#Basic String Operations
#we can declare a string either inside single quotes or double quotes
string1="HeLlo world"
string2='HELLO WORLD'
#One problem is we need to put a string within double quotes while writing it inside print statement
print("hello world")
#Finding the index in a string with help of character and "its Case Sensitive"
print(string1.index('l'))
#Finding the count of the particular character from a string and "its Case Sensitive"
print(string1.count('L'))
#Its like a substring function in java, used to display the desired characters from the string
print(string1[6:11])
#This operation is used to skip the characters within the desired set of characters
#For Example: in "Hello world", it skips second character each time through the end where we specify it
print(string1[0:11:2])
#For reversing the string "scope resolution symbol and -1", reverses the given string
print(string1[::-1])
#To change the string to uppercase
print(string1.upper())
#To change the string to lowercase
print(string1.lower())
#To find out string whether string is present or not using "startswith" and endswith function
#And returntype of the func is Boolean(true or false)
#Its case sensitive
print(string1.startswith("HeLlo"))
print(string1.endswith("asda"))
#To split string using spaces or some criteria
print(string1.split(" "))

s = "welcoma to pythonpgm"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index('a'))

# Number of a's should be 2
print("a occurs %d times" % s.count('a'))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

#Conditions
# "==" checks two objs are equal or not
x=2
if x==2:
    print("true")
# "is operator can also be used to check conditions"
if x is 2:
    print("true")

# "not" operator is also used to check negative conditions
print(not False)

#using "and" & "or" operators to check two conditions
#Strings are case sensitive
name="vicky"
age=24
if name=="vicky" and age==24:
    print("true")
else:
    print("false")

if name=="vicky" or age==20:
    print("true")
else:
    print("false")

# "in" operator is used to check the specifies obj in a list
name ="vicky"
if name in["vicky", "kumar"]:
    print("true")
else:
    print("false")


# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")


#LOOPS
#two types of loops in python "for" and "while"
number=[1,2,3,4,5]
for no in number:
    print("The number is %s"%no)

#there is another func "range" used to get the values within the range
#if we only give end range like 10, it gets the value from 0 to 9
for x in range(10):
    print(x)
# we can also get desired values within sepcified range
# If we specify the range like (5,10), it get from 5 to 9
for x in range(5,10):
    print(x)

# we can get the values within specified range with skipping the value
for x in range(0,10,2):
    print(x)

# While loops
count=0
while count<=5:
    print(count)
    count+=1

#break and continue statements
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

for x in range(10):
    if x%2 is 0:
        continue
    print(x)

# Using of else keyword for loops
# We can use the else statements in case of for or while loops fails, else block gets executed
# Note:  If break statement is executed inside for loop then the "else" part is skipped.
# Note: "else" part is executed even if there is a continue statement.
count=0
while(count<5):
    print(count)
    count+=1
else:
    print("count has reached the limit %d" %count)

for x in range(1,10):
    if x%5==0:
        break
    print(x)
else:
    print("since break statement is there x wont be printed")

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number==237:
        break
    if  number%2==1:
        print(number)


