n = 5
result = '1'
for i in range(n-1):
    prev = result
    result = ''
    j = 0
    while j < len(prev):
        curr = prev[j]
        count = 1
        j += 1
        while j < len(prev) and prev[j] == curr:
            count += 1
            j += 1
        result += str(count) + str(curr)
print(result)