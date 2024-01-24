#EXAMPLES FROM ARTICLE
#getting the data type
x = 5
print(type(x))

#setting the data type
x = "Hello World"                  #str
x = 20                             #int
x = 20.5                           #float
x = 1j                             #complex
x = ["apple", "banana", "cherry"]  #list
x = ("apple", "banana", "cherry")  #tuple
x = range(6)                       #range
x = {"name" : "John", "age" : 36}  #dict
x = {"apple", "banana", "cherry"}  #set
x = frozenset({"apple", "banana",  #frozenset
"cherry"})
x = True                           #bool
x = b"Hello"                       #bytes
x = bytearray(5)                   #bytearray
x = memoryview(bytes(5))           #memoryview
x = None                           #NoneType

#setting specific data type
x = str("Hello World")                  #str
x = int(20)                             #int
x = float(20.5)                           #float
x = complex(1j)                             #complex
x = list(("apple", "banana", "cherry")) #list
x = tuple(("apple", "banana", "cherry"))  #tuple
x = range(6)                       #range
x = dict(name = "John", age = 36)  #dict
x = set(("apple", "banana", "cherry"))  #set
x = frozenset(("apple", "banana",  #frozenset
"cherry"))
x = bool(5)                           #bool
x = bytes(5)                      #bytes
x = bytearray(5)                   #bytearray
x = memoryview(bytes(5))           #memoryview

#EXERCISE 1
x = 5
print(type(x))
int

#EXERCISE 2
x = "Hello World"
print(type(x))
str

#EXERCISE 3
x = 20.5
print(type(x))
float

#EXERCISE 4
x = ["apple", "banana", "cherry"]
print(type(x))
list

#EXERCISE 5
x = ("apple", "banana", "cherry")
print(type(x))

#EXERCISE 6
x = {"name" : "John", "age" : 36}
print(type(x))
dict

#EXERCISE 7
x = True
print(type(x))
bool