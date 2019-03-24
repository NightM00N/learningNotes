# 冒泡排序
def BubbleSort(L, n):# L待排数组；n排列区间
    exchange = n-1# 第一次排序的区间是[0, n-1]
    while exchange != 0:
        bound = exchange
        exchange = 0
        for i in range(bound):
            if L[i] > L[i+1]:
                # temp = L[i]
                # L[i] = L[i+1]
                # L[i+1] = temp
                L[i], L[i+1] = L[i+1], L[i]
                exchange = i
    return L

L = [7, 9, 2, 5, 4]
n = 5
result = BubbleSort(L, n)
print(result)# [2, 4, 5, 7, 9]