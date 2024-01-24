#EXAMPLES FROM THE ARTICLE
#creating variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
y = "Sally" #x is now of type str
print(x)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#get the type
x = 5
y = "John"
print(type(x))
print(type(y))

#single or double quotes
x = "John"
# is the same as
x = 'John'

#case-sensitive
a = 4
A = "Sally"
#A will not overwrite a

#variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#camel case
#each word, except first, starts with a capital letter:
myVariableName = "John"

#pascal case
#each word starts with a capital letter:
MyVariableName = "John"

#snake case
#each word is seperated by an underscore character:
my_variable_name = "John"

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#global variables
x = "aweaome"
def myfunc():
    print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#EXERCISE 1
carname = "Volvo"

#EXERCISE 2
x = 50

#EXERCISE 3
x = 5
y = 10
print(x + y)

#EXERCISE 4
x = 5
y = 10
z = x + y
print(z)

#EXERCISE 5
x, y, z = "Orange", "Banana", "Cherry"

#EXERCISE 6
x = y = z = "Orange"

#EXERCISE 7
def myfunc():
    global x
    x = "fantastic"