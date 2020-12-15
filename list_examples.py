s = '5;8;7;13'
SEPARATOR = ';'
parts = s.split(SEPARATOR)
sum = 0
for part in parts:
    number = int(part)
    sum += number
print(sum)

l = []
for i in range(2, 102, 2):
    l.append(i)
print(l)

l = [3, 25, 2, 35, 1]
counter = 0
for i in l:
    if i > 10:
        counter += 1
print(counter)

number = -1
numbers = []
while number != 0:
    number = int(input("Adj meg egy számot!\n"))
    if number != 0:
        numbers.append(number)
print(numbers)

if len(numbers) != 0:
    sum = 0
    for i in numbers:
        sum += i
    print(sum / len(numbers))

l = ['alma', 'korte', 'ab']
result = []
for i in l:
    if len(i) > 3:
        result.append(i)
print(result)