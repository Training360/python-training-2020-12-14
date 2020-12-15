from random import randrange

number = randrange(0, 100)
print("Number: " + str(number))

number_of_tries = 0
found = False
while not found:
    n = int(input("Adj meg egy pozitiv egesz szamot!\n"))
    number_of_tries += 1
    if n < number:
        print("Nagyobbra gondoltam!")
    elif n > number:
        print("Kissebbre gondoltam!")
    else:
        print("Eltalaltad " + str(number_of_tries) + " probalkozasbol.")
        found = True