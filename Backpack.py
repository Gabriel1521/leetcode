# 01 Backpack
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

print(dp)

for (i=1;i<=N;i++)
    for (j=M;j>=1;j--)
            date[j]=max(date[j],date[j-w[i]]+v[i]);

# Complete Backpack
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

for (i=1;i<=N;i++)
    for (j=w[i];j<=M;j++)
        date[j]=max(date[j],date[j-w[i]]+v[i]);

# Find item
void findWhat(int i, int j) {				//最优解情况
	if (i >= 0) {
		if (dp[i][j] == dp[i - 1][j]) {
			item[i] = 0;
			findWhat(i - 1, j);
		}
		else if (j - w[i] >= 0 && dp[i][j] == dp[i - 1][j - w[i]] + v[i]) {
			item[i] = 1;
			findWhat(i - 1, j - w[i]);
		}
	}
」
