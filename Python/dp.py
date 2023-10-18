# DP

# Climbing Stairs



# House Robber
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [0]*n
        if n <= 2:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]


# House Robber II
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        return max(self.dp(nums[1:]),self.dp(nums[:-1]))

    def dp(self,nums):
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]


# Integer Break
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        k = n//2
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2,n+1):
            if i != n:
                dp[i] = i
            else:
                dp[i] = float('-inf')
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],dp[j]*dp[i-j])
        return dp[-1]


# Minimum Path Sum
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]

# Unique Path
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

# Unique Path II
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1 - grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] * (1-grid[i][0])
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] * (1-grid[0][j])
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1-grid[i][j])
        return dp[-1][-1]

# Coin change
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0


        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]

# Coin change II

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not amount:
            return 1
        if not coins:
            return 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c,amount+1):
                dp[i] += dp[i-c]
        return dp[-1]

# 123. Best Time to Buy and Sell Stock III

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        min_price = prices[0]
        profit = 0
        profits = []
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i]-min_price)
            profits.append(profit)

        max_price = prices[-1]
        max_profit = 0
        total_return = 0
        for i in range(len(prices)-1,-1,-1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total_return = max(total_return, max_profit + profits[i])
        return total_return

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

# 714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0,-prices[0]
        for i in range(len(prices)):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash

# 309. Best Time to Buy and Sell Stock with Cooldown

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        cash, cash_cool, hold = 0,0,-prices[0]
        for p in prices:
            hold = max(hold, cash-p)
            cash = max(cash, cash_cool)
            cash_cool = hold+p
        return max(cash,cash_cool)
