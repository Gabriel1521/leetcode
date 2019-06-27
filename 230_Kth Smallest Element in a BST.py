# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s = []
        node = root
        i = 0

        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            i += 1
            if i == k:
                return node.val
            node = node.right

# averaged time complexity: log(n) + k
def kthSmallest(self, root, k):
    self.k = k
    self.res = 0
    self.helper(root)
    return self.res

def helper(self, root):
    if root:
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)
