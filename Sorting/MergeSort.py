
def MergeSort(a_list):
    #n = len(a_list)
    if len(a_list) > 1:
        mid = len(a_list)//2
        L = a_list[:mid]
        R = a_list[mid:]
        MergeSort(L)
        MergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a_list[k] = L[i]
                i += 1
            else:
                a_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a_list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a_list[k] = R[j]
            j += 1
            k += 1

    return(a_list)

a_list = [2, 4, 1, 5, 8, 0]
print(MergeSort(a_list))