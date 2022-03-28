x = 11
if x % 2 == 0:  # false
    print("Even number")
else:
    print("Odd number")

# postive or negative
num = 5
if num < 0:
    print(num, " is negative")
else:
    print(num, "is positive")

a = 10
b = 3
c = 5
if a < b and a < c:
    print("A is smaller")
elif b < a and b < c:  # else if
    print("B is smaller")
else:
    print("C is smaller")


x = 10
if x % 2 == 0:  # false
    pass
else:
    pass
