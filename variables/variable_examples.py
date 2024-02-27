a = 1
b = 2
c = 3.5
hi = "Hello World"
print(hi)

#equal sign assigns a value
print(type(a))
print(type(b))
print(type(c))
print(type(hi))

x = 5
y = x
print("before re-assign...")
print("Value of x:", x)
print("ID of x", id(x))

x = 6
print("reassigned")
print("new value:", x)
print("ID of x", id(x))
print("new value:", y)
print("ID of y", id(y))


#interestingly it remembers the id of x before re assignment
if you assign one variable the value of another it will be replaced

