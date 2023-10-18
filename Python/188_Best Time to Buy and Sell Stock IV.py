# 188. Best Time to Buy and Sell Stock IV

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k or not prices:
            return 0
        n = len(prices)

        # unlimited transactions
        # buy & sell on the same day
        if k > n/2:
            ans = 0
            for i in range(1,n):
                ans += max(0,prices[i]-prices[i-1])
            return ans

        dp = [[0 for _ in range(n)] for __ in range(k+1)]
        for i in range(1,k+1):
            lastMax = dp[i-1][0] - prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], prices[j] + lastMax)
                lastMax = max(lastMax,dp[i-1][j] - prices[j])
        return dp[k][-1]
