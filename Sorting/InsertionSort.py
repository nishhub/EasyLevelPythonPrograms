def insert_sort(a_list):

    for i in range(1, len(a_list)):
        temp = a_list[i]
        j = i-1
        while j >= 0 and temp < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = temp

    return a_list

a_list = [2, 4, 1, 5, 8, 0]
print(insert_sort(a_list))


