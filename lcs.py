# Longest common subsequence

def lcs(s1,s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for j in range(n+1)]for i in range(m+1)]
    print(len(dp),len(dp[0]))
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            elif dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

    for row in dp:
        print(row)

    i = m
    j = n
    print(s1)
    print(s2)
    l = []
    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            print(i,j)
            l.append(s1[i-1])
            i -= 1
            j -= 1
            print(l)
        if dp[i-1][j] == dp[i][j]:
            i -= 1
        if dp[i][j-1] == dp[i][j]:
            j -= 1

    l.reverse()
    s3 = "".join(l)
    print(s3)
    return dp[m][n]


def main():
    txt = "ABCDEFF"
    pat = "KLBCNKF"
    idx = lcs(txt,pat)
    print("IDX",idx)



if __name__ == '__main__':
    main()
