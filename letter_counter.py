def count_letters(s):
    """Visszaadja, hogy a paraméterben melyik betűből mennyi van"""
    result = {}
    for c in s:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


def print_alpha(c: dict):
    """A kulcsok szerint abc sorba rendezve írja ki a dict tartalmát"""
    keys_in_order = sorted(c.keys())
    for key in keys_in_order:
        print(f'{key}  {c[key]}')

# sorted() fuggvenyt kell hasznalni


number_of_letters = count_letters("szarvasmarhabaja")
print_alpha(number_of_letters)

