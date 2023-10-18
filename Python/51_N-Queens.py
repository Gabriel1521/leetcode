# 51. N-Queens

class Solution(object):
    def solveNQueens(self, n):
        res = []
        nums = [-1]*n
        self.dfs(nums,0,[],res)
        return res

    def dfs(self,nums,idx,path,res):
        n = len(nums)
        if idx == n:
            res.append(path)
            return
        for i in range(n):
            nums[idx] = i
            if self.isValid(nums,idx):
                s = "."*n
                self.dfs(nums,idx+1,path+[s[:i]+"Q"+s[i+1:]],res)

    def isValid(self,nums,n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True

# 52. N-Queens II

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        nums = [-1]*n
        self.dfs(nums,0)
        return self.res

    def dfs(self,nums,idx):
        if idx==len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[idx] = i
            if self.isValid(nums,idx):
                self.dfs(nums,idx+1)

    def isValid(self,nums,n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
