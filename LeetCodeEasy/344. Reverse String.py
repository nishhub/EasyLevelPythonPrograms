s = ["h","e","l","l","o"]

i = 0
j = len(s) -1
print(s)

while i < j/2:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
print(s)
