names = []  # ures lista

names = ["John Doe", "Jane Doe", "Jack Doe"]

john = ["John Doe", 28, "johndoe@example.com"]

print(names[0])
print(names[1])

# print(names[4])  # list index out of range

print(names[::-1])
print(names)

numbers = [1, 2, 3, 4, 5]
print(numbers)

print(len(numbers))

employees = [['John Doe', 1970], ['Jack Doe', 1980]]
print(employees[1][1])

for name in names:
    print(name)

print(3 in numbers)
print('Jack Smith' in names)

odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
print(odd_numbers + even_numbers)

print(odd_numbers * 3)

# s = "John Doe" nem modosithato = immutable
# s[3] = "X"

even_numbers[0] = 22  # modosithato - mutable
print(even_numbers)

even_numbers.clear()

print(even_numbers)