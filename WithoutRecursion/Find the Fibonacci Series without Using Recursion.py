a = 10
b = 5
n = 10
print(a, b)
while n-2 > 0:
    c = a+b
    b = c
    a = b
    n -= 1
    print(c)