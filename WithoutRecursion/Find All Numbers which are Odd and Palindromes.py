n = 100
a = [i for i in range(0, n) if i % 3== 0 and str(i) == str(i)[::-1]]
print(a)