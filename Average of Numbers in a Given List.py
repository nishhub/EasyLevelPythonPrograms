n = int(input("Enter the numbers of elements to be insert"))
a = []

for i in range(0, n):
    element = int(input("Enter a element"))
    a.append(element)

avg = sum(a)/n

print("The average of numbers in a list is", round(avg, 2))

