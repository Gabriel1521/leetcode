# 322. 零钱兑换

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount == 0:
            return 0
        dp = [amount+1]*(amount+1)

        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]

# 518. Coin Change 2

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount + 1):
                    dp[i] += dp[i - c]
        return dp[-1]
