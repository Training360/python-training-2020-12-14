from random import randrange, choice, Random


def random_string(chars, min_length, max_length, random=Random()):
    result = ""
    length = random.randrange(min_length, max_length)
    for i in range(length):
        c = random.choice(chars)
        result += c
    return result

print(random_string("xyz", 5, 20))