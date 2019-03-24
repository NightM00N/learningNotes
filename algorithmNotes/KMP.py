# 串匹配KMP算法
def GetNext(T, next):
    next[0] = -1
    for j in range(len(t)):
        for len in range(j):
            for i in range(len):
                if T[i] != T[j-len+i]:
                    break
        if len < 1:
            next[j] = 0
def KMP(S, T):
    pass