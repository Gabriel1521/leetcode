# 312.Burst Balloons

# 通过在头尾加上1求解中间问题，实际求解的是去除头尾的最大值
# 每次决定最后的balloon然后再和子问题的解一起构成当前interval的解

class Solution(object):
       def maxCoins(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          nums = [1] + nums + [1]
          n = len(nums)
          dp = [[0] * n for _ in xrange(n)]

          def calculate(i, j):
              if dp[i][j] or j == i + 1: # in memory or gap < 2
                    return dp[i][j]
              coins = 0
              for k in xrange(i+1, j): # find the last balloon
                    coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
              dp[i][j] = coins
              return coins

        return calculate(0, n-1)
