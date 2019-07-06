
# 99. Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res = []
        self.helper(root, res)
        first, second = None, None
        for i in xrange(1, len(res)):
            if not first and res[i-1].val > res[i].val:
                first, second = res[i-1], res[i]
            if first and res[i-1].val > res[i].val:
                second = res[i]
        first.val, second.val = second.val, first.val

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root)
            self.helper(root.right, res)
