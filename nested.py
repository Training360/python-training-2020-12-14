number = int(input("Adj meg egy szamot"))

if number < 100:
    print("Kisebb mint szaz")
    if number % 2 == 0:
        print("Paros")
    else:
        print("Paratlan")