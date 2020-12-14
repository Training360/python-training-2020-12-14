b = True
print(b)
print(type(b))

print(5 == 5)
print(5 == 6)

i = 6
j = 7
print(i == j)

n = 5
print(n == 5)

x = y = 6  # y = 6 x = y
print(str(x) + str(y))
x = (y == 6)  # tmp1 = y == 6 x = tmp1
print(str(x) + str(y))

print('ab' == 'ab')
print('ba' == 'ab')

print(5 != 6)
print(6 != 6)  # False

print(5 < 6)
print(6 < 5)
print(5 <= 5)

print(5 <= (5 + 5))
a = 5
print(5 <= a)
print(5 <= len('alma'))

print((a % 2) == 0)
print((a % 5) == 0)

a = 5
print((a > 0))

if not (6 % 2 == 0):
    print("Paratlan")
    print("Ez")
else:
    print("Ez paros")
print("A szam")
print("Hello")