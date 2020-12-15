# Unit test
# Függvény, ami másik függvényt tesztel
from calc import add


def test_add():
    # BDD - Behaviour driven development
    # Három rész: given - when - then (assert)

    # given
    input_n = 5
    input_m = 6

    # when - függvény hívása
    actual_value = add(input_n, input_m)

    # then - aktuális érték megfelelő-e
    assert actual_value == 11


def test_negative_add():
    assert add(-2, -3) == -5