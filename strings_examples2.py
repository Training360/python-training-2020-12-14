from random import randrange

for i in range(5):
    n = randrange(1, 10000 + 1)
    number_of_spaces = 5 - len(str(n))
    s = number_of_spaces * " " + str(n)
    print(s)

s = "arvizturoTUKORFUROGEP"
#s = "gfgfddfgdhfdh"
VOWELS = 'aeiou'
# contains = False
number_of_vowels = 0
for c in s.lower():
    if c in VOWELS:
        # contains = True
        number_of_vowels += 1

if number_of_vowels > 0:
    print("van benne: " + str(number_of_vowels))