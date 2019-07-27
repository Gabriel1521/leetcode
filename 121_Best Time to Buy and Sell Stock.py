# 121. Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_num = 0, float('inf')
        for price in prices:
            min_num = min(min_num,price)
            profit = price-min_num
            max_profit = max(profit, max_profit)
        return max_profit


# 122. Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# 123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profits = []
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit, price-min_price)
            profits.append(max_profit)

        max_price = prices[-1]
        max_profit = 0
        total_profit = 0
        for i in range(len(prices)-1,-1,-1):
            max_price = max(prices[i], max_price)
            max_profit = max(max_profit, max_price - prices[i])
            total_profit = max(total_profit, max_profit+profits[i])
        return total_profit
