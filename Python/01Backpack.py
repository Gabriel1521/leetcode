#01 backpack

w = [0,2,3,4,5]
v = [0,3,4,5,6]
m = 4
c = 8
dp = [[0 for j in range(c+1)]for i in range(m+1)]

for i in range(1,m+1):
	for j in range(1,c+1):
		if j < w[i]:
			dp[i][j] = dp[i-1][j]
		else:
			if dp[i-1][j] > dp[i-1][j-w[i]] + v[i]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j-w[i]] + v[i]
