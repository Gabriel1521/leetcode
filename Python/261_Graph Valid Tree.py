# 261. Graph Valid Tree

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        ds = DisjointSet()

        for i in range(n):
            ds.make_set(i)

        for edge in edges:
            if ds.union(edge[0], edge[1])==False:
                return False

        return len(edges)==n-1

class Node(object):
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank

class DisjointSet(object):
    def __init__(self):
        self.map = {}
        self.num_sets = 0

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.map[data] = node
        self.num_sets += 1

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)

        if parent1.data == parent2.data:
            return

        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2

        self.num_sets -= 1

    def find_set(self, data):
        return self.find_set_util(self.map[data])


    def find_set_util(self, node):
        if parent != node:
            node.parent = find_set(node.parent)
        return node.parent
