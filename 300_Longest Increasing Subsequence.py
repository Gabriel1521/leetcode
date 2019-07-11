# 300. Longest Increasing Subsequence

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)

        n = max(dp)
        return n

# 128. Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0

        while nums:
            n = nums.pop()
            l1 = l2 = 0

            k = n+1
            while k in nums:
                nums.remove(k)
                l1 += 1
                k += 1

            k = n-1
            while k in nums:
                nums.remove(k)
                l2 += 1
                k -= 1

            max_len = max(max_len,l1+l2+1)
        return max_len
