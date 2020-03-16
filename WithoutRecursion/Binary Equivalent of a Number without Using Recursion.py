n = 2
a = []
while n > 0:
    remain = n % 2
    a.append(remain)
    n //= 2

print(a[::-1])