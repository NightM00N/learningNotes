# 合并两个升序序列
def union(A, B):
    i = 0
    j = 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    while i < len(A):
        result.append(A[i])
        i += 1
    while j < len(B):
        result.append(B[j])
        j += 1
    return result


A = [1,3,5,7,9]
B = [2,4,6,8,10]
print(union(A,B))