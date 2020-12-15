def collect_even_numbers(numbers):
    result = []
    for i in numbers:
        if is_even(i):
            result.append(i)
    return result


def is_even(number):
    return number % 2 == 0


print(collect_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))

print(collect_even_numbers([11, 12, 13, 14, 15]))
