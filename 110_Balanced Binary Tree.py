# 110. Balanced Binary Tree

class Solution(object):
    def isBalance(self, root):
      if not root:
        return True

      return abs(self.getHeight(root.left)-self.getHeight(root.right))<2 and self.isBalance(root.left) and self.isBalance(root.right)

    def getHeight(self, root):
      if not root:
        return True

      return 1 + max(self.getHeight(root.left),self.getHeight(root.right))


# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
