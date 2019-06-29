# 46. Permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self,nums, path,res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)

# 47. Permutations II

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.permutation(nums,[],res)
        return res


    def permutation(self,nums,path,res):
        if len(nums) == 0:
            if path not in res:
                res.append(path)
            return
        for i in range(len(nums)):
            self.permutation(nums[:i]+nums[i+1:],path+[nums[i]],res)
