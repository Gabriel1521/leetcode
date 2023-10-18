# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict()
        i = 0
        while i < len(nums):
            if nums[i] not in d:
                d[nums[i]] = 1
            elif d[nums[i]] == 2:
                nums.remove(nums[i])
                continue
            elif d[nums[i]] == 1:
                d[nums[i]] += 1
            i += 1
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        if l<2:
            return l
        i=2
        for num in nums[2:]:
            if num!=nums[i-2]:
                nums[i]=num
                i+=1
        return i
