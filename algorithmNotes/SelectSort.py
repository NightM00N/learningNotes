#选择排序
def SelectSort(L):
    for i in range(len(L)):
        index = i
        for j in range(i+1, len(L)):
            if L[j] < L[index]:
                index = j
        if index != i:
            L[i], L[index] = L[index], L[i]
    return L
arr = [1, 4, 5, 3, 2]
print(SelectSort(arr))