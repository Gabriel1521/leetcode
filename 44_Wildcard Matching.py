# 44. Wildcard Matching

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1, l2 = len(s), len(p)
        dp = [[False for j in range(l2+1)] for i in range(l1+1)]
        dp[-1][-1] = True

        for i in range(l1,-1,-1):
            for j in range(l2-1,-1,-1):
                if i < l1 and (s[i] == p[j] or p[j] == '?'):
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*':
                    if i < l1:
                        dp[i][j] = dp[i+1][j] or dp[i][j+1]
                    else:
                        dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = False
        return dp[0][0]

        
