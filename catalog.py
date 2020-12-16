catalog = {"apple": 5, "banana": 10}
print(type(catalog))

print(catalog['apple'])

catalog['orange'] = 15

print(catalog)

catalog['orange'] = 20

print(catalog)

catalog['orange'] = catalog['orange'] + 1

print(catalog)

del catalog['orange']
print(catalog)

print("alma")

for k in catalog.keys():
    print(k)
for v in catalog.values():
    print(v)

for (k,v) in catalog.items():
    print(k + "   " + str(v))

print("apple" in catalog)
print("dog" in catalog)