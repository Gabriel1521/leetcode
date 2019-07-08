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
