s = "alma"
i = len(s) - 1
reversed = ""
while i >= 0:
    reversed += s[i]
    i -= 1
print(reversed)

s = "alma"
i = len(s) - 1
reversed = ""
while i >= 0:
    reversed += s[i]
    i -= 1
if s == reversed:
    print("Palindroma")
else:
    print("Nem palindroma")

stared = ""
for c in "alma":
    if stared != "":
        stared += "*"
    stared += c
print(stared)

i = 1
chars = ""
while i < len(stared):
    chars += stared[i]
    i += 2
print(chars)

chars = ""
for i in range(1, len(stared), 2):
    chars += stared[i]
print(chars)