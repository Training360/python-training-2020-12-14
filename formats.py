# old-style, C programozási nyelv

print("A %s eletkora %10.2f" % ('John Doe', 10.10))

# format metódus

print("A {0} eletkora {1}".format('John Doe', 23))

print("A {name} eletkora {age:>10}".format(name='John Doe', age=23))

# 3.6 Python - String interpolation

name = 'John Doe'
age = 18
print(f'A {name} eletkora {age:>10}, matek: {10 + 20}')



