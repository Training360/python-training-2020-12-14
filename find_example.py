def find_all(s: str, sub: str) -> list:
    """Megkeresi az elso parameterkent atadott stringben a masodik substringet."""
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


result = find_all("alma", "a")
print(type(result))
