# 958. Check Completeness of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque([(root, 1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2*coord))
            if u.right:
                q.append((u.right, 2*coord+1))
        return len(res) == res[-1]
