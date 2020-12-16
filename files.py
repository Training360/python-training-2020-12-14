def write_hello():
    with open("hello.txt", "w") as file:
        file.write("hello\n")
        # algoritmus
        file.write("python\n")
    print("end")

# Írjátok ki egy fájlba a kettes szorzótáblát 1*2 - 10*2 (sortöréssel elválasztva)

def write_table():
    with open("table.txt", "w") as file:
        for i in range(1, 11):
            file.write(f'{i:>2} * 2 = {i * 2:>2}\n')

# Írjatok egy függvényt, ami alkalmazottak listáját kapja.
# {"name" = "John Doe", "year" = 1970}
# Feladat: írjátok ki a lista tartalmát egy szöveges CSV állományba
# name;year
# John Doe;1970

def write_employees(employees):
    FIELDS = ['name', 'year']
    with open("employees.csv", "w") as file:
        file.write("name,year\n")
        for employee in employees:
            counter = 0
            for field in FIELDS:
                file.write(str(employee[field]))
                if (counter < len(FIELDS) - 1):
                    file.write(";")
                counter += 1
            file.write("\n")

# write_table()
write_employees([{"name": "John Doe", "year": 1970}, {"name": "Jane Doe", "year": 1970},{"name": "Jack Doe", "year": 1970}])