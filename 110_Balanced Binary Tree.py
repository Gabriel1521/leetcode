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

# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = collections.deque([root])
        res = []
        while queue:
            cur_level, size = [],len(queue)
            for i in range(size):
                node = queue.popleft()
                if node:
                    cur_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    cur_level.append(None)
            res.append(cur_level)

        for i in range(1,len(res)):
            mid = len(res[i])//2
            a = res[i][:mid]
            b = res[i][mid:][::-1]
            if a != b:
                return False
        return True

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L,R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left,R.right) and isSym(L.right,R.left)
            return False
        return isSym(root,root)
