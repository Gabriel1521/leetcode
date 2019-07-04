# 200. Number of Islands

#DFS
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        tag = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    tag += 1
                    self.dfs(grid, i, j,tag)

        return (tag-1)

    def dfs(self, grid, i, j, tag):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = tag
        self.dfs(grid, i+1, j,tag)
        self.dfs(grid, i-1, j,tag)
        self.dfs(grid, i, j+1,tag)
        self.dfs(grid, i, j-1,tag)

#BFS

class Solution(object):
    def numIslands(self, grid):
        queue = collections.deque([])
        tag = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    queue.append([i,j])
                    tag = tag+1
                    while queue:
                        x,y = queue.popleft()
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == '1':
                            grid[x][y] = str(tag)
                            queue.append([x+1,y])
                            queue.append([x-1,y])
                            queue.append([x,y+1])
                            queue.append([x,y-1])

        return tag-1
