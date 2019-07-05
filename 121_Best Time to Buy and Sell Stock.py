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
