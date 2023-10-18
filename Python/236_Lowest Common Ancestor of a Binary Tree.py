#236. Lowest Common Ancestor of a Binary Tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
