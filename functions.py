# Fgv. deklaráció
# Formális paraméter = adott függvény lokális változója
def print_three_times(times=3, message="Python"):
    """Kiirja haromszor, hogy Python"""

    # i változó is a függvény lokális változója
    for i in range(times):
        print(message)


def add(n, m):
    print_three_times(n + m, "osszeadas!!! :)")
    return n + m


# Hívás
# print("start")
# print_three_times(3, "Python")  # Aktuális paraméter
# print("szun")
# print_three_times(5, "Java")
# print_three_times(1, "JavaScript")
# print("end")
#
# print(add(5, add(1, 3)))
# print(add(8, 2))

print_three_times(message="JavaScript", times=10)