n = 4
c = 10
w = [0,2,3,4,7]
v = [0,1,3,5,9]

dp = [[0 for j in range(c+1)]for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,c+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])

print(dp[-1][-1])

# j >= w[i] max(dp[i-1][j],dp[i][j-w[i]]+v[i])
# j < w[i] dp[i-1][j]
