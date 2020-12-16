def find_max_and_min(l: list) -> tuple:
    min = l[0]
    max = l[0]
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)


# tuple: adatszerkezet
numbers = (1, 2, 3, 4, 5)
print(numbers[2])
print(numbers[::-1])

# Különbség: immutable!
#number[0] = 999 # NEM MUKODIK
print(type(numbers))

employee = ('John Doe', 1980, 'johndoe@example.com')
print(employee[0])
print(employee[1])
print(employee[2])

(x, y) = (5, 6)
print(x)
print(y)

# Kikeresni a max és min elemet
print(find_max_and_min([7, 6, 4, 8, 1, 6]))

employees = (("John Doe", 1980), ("Jack Doe", 1990), ("Jane Doe", 1985))
for (name, year) in employees:
    print(name + " szuletesi ev: " + str(year))

names = ("John Doe", "Jane Doe", "Jack Doe")
for (i, name) in enumerate(names, 1):
    print(str(i) + "    " + name)
