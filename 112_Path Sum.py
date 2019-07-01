# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        s = [(root, root.val)]
        while s:
            node, val = s.pop()
            if not node.left and not node.right:
                if val == sum:
                    return True
            else:
                if node.right:
                    s.append((node.right,val+node.right.val))
                if node.left:
                    s.append((node.left,val+node.left.val))
        return False
