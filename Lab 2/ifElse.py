#EXERCISE 1
a = 50
b = 10
if a > b:
    print("Hello World")

#EXERCISE 2
a = 50
b = 10
if a != b:
    print("Hello World")

#EXERCISE 3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

#EXERCISE 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

#EXERCISE 5
if a == b and c == d:
    print("Hello")

#EXERCISE 6
if a == b or c == d:
    print("Hello")

#EXERCISE 7
if 5 > 2:
    print("YES")

#EXERCISE 8
a = 2
b = 5
print("YES") if a == b else print("NO")

#EXERCISE 9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#EXAMPLES FROM ARTICLES
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#pass
a = 33
b = 200
if b > a:
  pass