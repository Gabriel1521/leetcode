# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = set([])
        for i in range(len(nums)-2):
            num1 = nums[i]
            l = i+1
            r = len(nums) -1
            while l<r:
                s = num1 + nums[l] + nums[r]
                if s == 0:
                    res = (num1,nums[l],nums[r])
                    result.add(res)
                    l+=1
                    r-=1

                elif s>0:
                    r-=1
                else:
                    l+=1



        return list(result)


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = set([])

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    path = (nums[i],nums[l],nums[r])
                    res.add(path)
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)

# 1. 两数之和


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        res = []
        for i in range(len(nums)):
            if nums[i] in d:
                res = [d[nums[i]],i]
            else:
                r = target - nums[i]
                d[r] = i
        return res
