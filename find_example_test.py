from find_example import find_all


def test_find_one():
    assert find_all("almakorte", "al") == [0]


def test_find_twice():
    assert find_all("almakorte", "a") == [0, 3]


def test_find_twice_two_char():
    assert find_all("almaalmaalma", "al") == [0, 4, 8]


def test_last():
    assert find_all("almaalmaalmaal", "al") == [0, 4, 8, 12]


def test_last_empty_string():
    assert find_all("", "al") == []


def test_last_empty_substring():
    assert find_all("", "") == []
