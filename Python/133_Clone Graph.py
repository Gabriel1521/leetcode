# 133. Clone Graph


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = Node(node.val,[])
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val,[])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = dict()

        visited[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[cur].neighbors.append(visited[neighbor])
        
        return visited[node]