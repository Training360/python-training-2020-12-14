s = "rozsomak"

print("oz" in s)
print("xy" in s)

print(s.find('o'))
print(s.find('o', 2))

# Írj egy findAll(s, sub) függvényt, mely visszaadja egy listában,
# hogy a keresett karakter hanyadik pozíciókon található.
# "rozsomak", "o" -> [1, 4]
# Írjatok hozzá tesztesetet!