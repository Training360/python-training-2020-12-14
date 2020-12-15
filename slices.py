s = "szarvasmarhacsaladfakutatas"
print(s[4])

print(s[4:8])

print(s[4:])

print(s[:4])

print(s[::2])

print(s[10:17:2])

print(s[20:0:-1])

print(s[::-1])

print(s == s[::-1])

print("al" in "alma")
print("xx" in "alma")

s = "szarvasmarhacsaladfakutatas"

print(s.find("marha"))
print(s.find("tehen"))

template = "Az en nevem {0}".format("Istvan")
print(template)

template = "A szam: {0}".format(999)
print(template)

template = "A szam: {0} es {1}".format(999, 888)
print(template)

