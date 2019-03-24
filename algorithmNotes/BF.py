#BF算法，串匹配
def BF(S, T):
    index = 0
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            index += 1
            i = index
            j = 0
    if j == len(T):
        return index + 1
    else:
        return 0

A = "aaaaaaaaaab"
B = "aaab"
print(BF(A, B))