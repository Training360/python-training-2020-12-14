def check_name(name: str) -> bool:
    valid = True
    if (len(name) < 2):
        valid = False
    else:
        if (len(name) > 20):
            valid = False
        else:
            if not name[0] == name[0].upper():
                valid = False
            else:
                valid = True

def check_name_eff(name: str) -> bool:
    if (len(name) < 2):
        return False
    if (len(name) > 20):
        return False
    if not name[0] == name[0].upper():
        return False

    return True