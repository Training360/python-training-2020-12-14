MAX = 50
s = ""
for i in range(0, MAX):
    if i % 15 == 0:
        s += "FizzBuzz"
    elif i % 3 == 0:
        s += "Fizz"
    elif i % 5 == 0:
        s += "Buzz"
    else:
        s += str(i)
    s += ", "
print(s)
