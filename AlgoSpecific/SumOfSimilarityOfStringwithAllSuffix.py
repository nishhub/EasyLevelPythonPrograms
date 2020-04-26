#!/bin/python3


def stringSimilarity(s, n , Z):
    l = r = 0
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r] == s[r-l]:
                r += 1
            Z[i] = r -l
            r -= 1

        else:
            k = i -l
            if Z[k] < r-i+1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and s[r] == s[r-l]:
                    r += 1
                Z[i] = r-l
                r -= 1
    return Z



def sumSimilarity(s):
    n = len(s)
    Z = [0 for i in range(n)]
    stringSimilarity(s, n, Z)
    total = n
    for i in range(n):
        total += Z[i]
    return total




s = "aaabaab"

print(sumSimilarity(s))
