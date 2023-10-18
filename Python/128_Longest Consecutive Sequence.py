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
