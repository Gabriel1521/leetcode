# KMP

def kmp(t, p):
    m = len(t)
    n = len(p)

    f = FailureFunction(p)
    i = 0
    j = 0
    res = []

    while i < m:
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == n:
            res.append(i-j)
            j = 0
            i += 1
            # return (i-j)
        elif i < m and p[j] != t[i]:
            if j != 0:
                j = f[j-1]
            else:
                i += 1
    return res
    #return -1

def FailureFunction(p):
    n = len(p)
    f = [0 for i in range(n)]
    i = 1
    j = 0
    while i<n:
        if p[i] == p[j]:
            j += 1
            f[i] = j
            i += 1
        else:
            if j > 0:
                j = f[j-1]
            else:
                f[i] = 0
                i += 1
    return f


def main():
    txt = "TEST IS A TEST TEST"
    pat = "TEST"
    a = kmp(txt,pat)
    print("IDX",a)



if __name__ == '__main__':
    main()
