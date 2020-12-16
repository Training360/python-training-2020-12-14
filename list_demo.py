def is_list_ordered(l: list) -> bool:
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


print(is_list_ordered([1, 2, 5, 7, 9]))
print(is_list_ordered([1, 2, 5, 4, 9]))
print(is_list_ordered([]))
print(is_list_ordered([1]))
print(is_list_ordered([5, 1, 6, 7, 8]))
print(is_list_ordered([1, 6, 7, 8, 2]))