#EXERCISE 1
print(10 > 9)
True

#EXERCISE 2
print(10 == 9)
False

#EXERCISE 3
print(10 < 9)
False

#EXERCISE 4
print(bool("abc"))
True

#EXERCISE 5
print(bool(0))
False

#EXAMPLES FROM ARTICLE
#booleean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#evaluate values and variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#most values are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#function can return a boolean
def myFunction():
    return True
print(myFunction())

def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))
