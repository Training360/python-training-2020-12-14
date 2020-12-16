with open("numbers.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())