def find_all(s, sub):
    if sub == "":
        return []
    result = []
    for i in range(len(s) - len(sub) + 1):
        part = s[i: i + len(sub)]
        if part == sub:
            result.append(i)
    return result


def find_all_2(s, sub):
    if sub == "":
        return []
    result = []
    find_index = 0
    while find_index != -1:
        find_index = s.find(sub, find_index)
        if find_index > -1:
            result.append(find_index)
            find_index += 1
    return result


print(find_all("almakorte", "al"))
print(find_all("almakorte", "a"))
print(find_all("almaalmaalma", "al"))
print(find_all("almaalmaalmaal", "al")) # Boundary value analysis
print(find_all("", "al")) # Boundary value analysis
print(find_all("", "")) # Boundary value analysis

print("\n")

print(find_all_2("almakorte", "al"))
print(find_all_2("almakorte", "a"))
print(find_all_2("almaalmaalma", "al"))
print(find_all_2("almaalmaalmaal", "al")) # Boundary value analysis
print(find_all_2("", "al")) # Boundary value analysis
print(find_all_2("", "")) # Boundary value analysis