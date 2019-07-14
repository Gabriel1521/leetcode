# 31. Next Permutation
# 首先从右边找到递增的两项
# 将递增左边的那一位和右边开始刚好比它大的数字交换
# 将递增左边的那一位右边的数列反转由降序变成升序来求最接近数列

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        #find the ascending item
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        #if all descending reverse string
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        #find the last ascending item
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        #reverse the later part
        l,r = k+1,len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
