# 77. Combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n+1)]
        res = []
        self.dfs(nums,k,0,[],res)
        return res

    def dfs(self,nums,k,idx,path,res):
        if k == 0:
            res.append(path)
            return # backtracking
        for i in xrange(idx, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)
