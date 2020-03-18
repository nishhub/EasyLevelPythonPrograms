def bubble_sort(a_list):
    swap = True

    for i in range(len(a_list)-1, 0, -1):
        for j in range(0, i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                swap = False
        if swap:
            return


a_list = [4, 2, 38, 10, 5]

bubble_sort(a_list)
print(a_list)