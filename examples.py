# n = int(input("Adj meg egy szamot!\n"))
# if n < 0:
#     print('Negativ')
# else:
#     print('Pozitiv')

# n = int(input("Adj meg egy szamot!\n"))
# if n % 2 == 0:
#     print('Paros')
# else:
#     print('Paratlan')

# name = input("Add meg a neved!\n")
# n = int(input("Adj meg egy szamot!\n"))

# for i in range(n):
#     print(name)

# print((name + "\n") * n)
# NUMBER_TO_CHECK = 3
#
# number = input("Adj meg egy szamot!")
# i = 0
# for c in number:
#     digit = int(c)
#     prefix = str(i) + ". szamjegy "
#     if digit < NUMBER_TO_CHECK:
#         print(prefix + "kisebb")
#     elif digit > NUMBER_TO_CHECK:
#         print(prefix + "nagyobb")
#     else:
#         print(prefix + "pont " + str(NUMBER_TO_CHECK))
#     i = i + 1

# text = input("Adj meg egy szoveget!")
# for c in text:
#     if c == 'x':
#         print('x')

word = input("Adj meg egy szot!")
reversed = ''
print(len(reversed))
for c in word:
    reversed = c + reversed
print(reversed)