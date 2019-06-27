# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.curmaxv = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recurPathSum(root)
        return self.curmaxv


    def recurPathSum(self,root):
        if not root:
            return 0
        left = max(0, self.recurPathSum(root.left))
        right = max(0, self.recurPathSum(root.right))
        self.curmaxv = max(left+right+root.val, self.curmaxv)
        return max(left, right) + root.val
