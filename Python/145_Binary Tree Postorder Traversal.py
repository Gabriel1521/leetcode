# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return 
        
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        res.append(node.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = [(root,0)]

        while s:
            node, v= s.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    s.append((node, 1))
                    s.append((node.right, 0))
                    s.append((node.left, 0))
        return res