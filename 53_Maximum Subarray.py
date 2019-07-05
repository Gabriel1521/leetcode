
# 53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum+num)
            maxSum = max(curSum, maxSum)
        return maxSum


# 152. Maximum Product Subarray

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MinTemp = nums[0]
        MaxTemp = nums[0]
        Max = nums[0]
        for i in xrange(1, len(nums)):
            MinTemp, MaxTemp = min(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp), max(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp)
            Max = max(Max, MaxTemp)
        return Max
