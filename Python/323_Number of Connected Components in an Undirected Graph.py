# 323. Number of Connected Components in an Undirected Graph

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ds = Disjointset()
        for i in range(n):
            ds.make_set(i)

        for edge in edges:
            ds.union(edge[0],edge[1])

        return ds.num_sets

class Node(object):
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank

class Disjointset(object):
    def __init__(self):
        self.map = {}
        self.num_sets = 0

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        node.rank = 1
        self.map[data] = node
        self.num_sets += 1

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        parent1 = self.find_set(node1)
        parent2 = self.find_set(node2)

        if parent1 == parent2:
            return

        if parent1.rank <= parent2.rank:
            if parent1.rank == parent2.rank:
                parent2.rank += 1
            parent1.parent = parent2
        else:
            parent2.parent = parent1

        self.num_sets -= 1

    def find_set(self, node):
        if node.parent != node:
            node.parent = self.find_set(node.parent)
        return node.parent
