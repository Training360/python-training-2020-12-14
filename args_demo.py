from sys import argv

print(argv)
for (i, arg) in enumerate(argv):
    print(f'{i:>5}. parameter: {arg}')