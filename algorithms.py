# Összegzés tétele
# Összeadja a listának az elemeit
from random import shuffle, choices, choice

l = [1, 3, 5, 7, 9, 12]
sum = 0
for i in l:
    sum += i
print(sum)


# Számlálás tétele
# feltételnek megfelelő elemek száma
l = [1, 3, 5, 7, 9, 12]
count = 0
for i in l:
    if i % 2 == 0:
        count += 1
print(count)

# Szélsőérték keresés tétele
#l = ["a", "aaa", "wqwqewqwqe", "aaaa", "asadasa"]
#max = ''
l = [12, 5, 8, 10, 2, 5, 8]
if len(l) > 0:
    min = l[0]
    max = l[0]
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
    print(min)
    print(max)

## Eldöntés tétel
l = ["Alma", "Korte", "Meggy", "Narancs"]
all_capitalized = True
for i in l:
    print("Vizsgalja: " + i)
    if i[0] != i[0].upper():
        print("Szabalyszego")
        all_capitalized = False
        break

print(all_capitalized)

## Szűres
years = [1987, 1920, 2010, 1970, 1960, 1980, 1985]
filtered = []
for i in years:
    if i > 1980:
        filtered.append(i)
print(filtered)

# Python: struktúrálatlan, stuktúrált, objektumorientált, funkcionális

## Transzformáció (map - leképezés)
words = ["alma", "korte", "meggy", "birsalma"]
lengths = []
for i in words:
    lengths.append(i[0].upper())
print(lengths)

# Kombinálva

# Csak a nagybetűsek maximális hosszát
words = ["alma", "Korte", "meggy", "birsalma", "Narancs"]
max = 0
for i in words:
    if i[0] == i[0].upper():
        if len(i) > max:
            max = len(i)
print(max)

# Rendezés
words = ["alma", "Korte", "meggy", "birsalma", "Narancs"]
words.sort()
print(words)

years = [1987, 1920, 2010, 1970, 1960, 1980, 1985]
years.sort()
print(years)

# Megkavarás
years = [1920, 1960, 1970, 1980, 1985, 1987, 2010]
shuffle(years)
print(years)

# Válassz véletlenszerűen

result = choice(years)
print(result)

mylist = ["apple", "banana", "cherry"]
print(choices(mylist, weights=[10, 1, 1], k=14))
