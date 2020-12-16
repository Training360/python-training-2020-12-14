def read_numbers():
    with open("numbers.txt", "r") as file:
        for line in file.readlines():
            print(line.strip())


def read_employees() -> list:
    employees = []
    with open("employees_input.csv", "r", encoding="UTF8") as file:
        c = 0
        for line in file.readlines():
            if c != 0:
                employee = {}
                parts = line.strip().split(",")
                employee['name'] = parts[0]
                employee['year'] = parts[1]
                employee['city'] = parts[2]
                employees.append(employee)
            c += 1
    return employees

employees = read_employees()
print(employees)
print(employees[2]['city'])