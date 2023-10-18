# 695. Max Area of Island

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        tag = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid,i,j,tag)
                    tag += 1
        d = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    if grid[i][j] in d:
                        d[grid[i][j]] += 1
                    else:
                        d[grid[i][j]] = 1
        if not d:
            return 0
        else:
            l = max(d.values())
            return l


    def dfs(self,grid,i,j,tag):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        if grid[i][j] == 1:
            grid[i][j] = tag
            self.dfs(grid,i-1,j,tag)
            self.dfs(grid,i+1,j,tag)
            self.dfs(grid,i,j-1,tag)
            self.dfs(grid,i,j+1,tag)
