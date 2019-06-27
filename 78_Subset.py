#78_Subset I
class Solution(object):
    def subsets(self, nums):
        res = []
        nums = sorted(nums)
        self.dfs(nums,0,[],res)
        return res

    def dfs(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx,len(nums)):
            self.dfs(nums, i+1, path+nums[i], res)


#90_Subsets II

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)
