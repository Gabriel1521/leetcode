# 72. Edit Distance
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)+1
        l2 = len(word2)+1

        dp = [[0 for j in range(l2)]for i in range(l1)]

        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j

        for i in range(1,l1):
            for j in range(1,l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)

        return dp[-1][-1]

        
