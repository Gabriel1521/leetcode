# 270. Closest Binary Search Tree Value


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        if abs(a-target)<abs(b-target):
            return a
        else:
            return b


# 272. Closest Binary Search Tree Value II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        q = []
        self.dfs(root,q,target)
        res = []
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res

    def dfs(self,root,q,target):
        if not root:
            return
        self.dfs(root.left,q,target)
        heapq.heappush(q,[abs(root.val-target),root.val])
        self.dfs(root.right,q,target)
