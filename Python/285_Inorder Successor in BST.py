# 285. Inorder Successor in BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        s = []
        node = root
        ans = 0
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            print(node.val)
            if ans == 1:
                return node
            if node == p:
                ans = 1
            node = node.right
        return None
