class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]* n
        res = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, isConnected)
                res += 1
        return res

    def dfs(self, i, visited, isConnected):
        n = len(visited)
        visited[i] = True

        for j in range(n):
            if isConnected[i][j] and not visited[j]:
                self.dfs(j, visited, isConnected)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        # 统计不同根的数量
        return sum(1 for i in range(n) if uf.parent[i] == i)

class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1