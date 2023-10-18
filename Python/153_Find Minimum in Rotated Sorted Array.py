# 153. Find Minimum in Rotated Sorted Array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i<j:
            m = (i+j)//2
            if nums[m] > nums[j]:
                i = m+1
            else:
                j = m
        return nums[i]

# 154. Find Minimum in Rotated Sorted Array II

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l<=h:
            while l< h and nums[l] == nums[l+1]:
                l += 1
            while l< h and nums[h] == nums[h-1]:
                h -=1
            while l == h:
                return nums[l]

            m = (l+h)//2
            if nums[m] > nums[h]:
                l = m+1
            else:
                h = m

        return nums[l]
