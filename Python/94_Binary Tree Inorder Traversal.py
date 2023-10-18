# 94 Binary Tree Inorder Traversal

# Stack
class Solution(object):
            def inorderTraversal(self, root):
                res,s = [],[(root,False)]
                while s:
                    node,v = s.pop()
                    if node:
                        if v:
                            res.append(node.val)
                        else:
                            s.append((node.right,False))
                            s.append((node,True))
                            s.append((node.left,False))
                return res

# Recursion
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        self.dfs(root.left,res)
        res.append(root.val)
        self.dfs(root.right,res)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            # 看右子树
            p = tmp.right
        return res


#144. 二叉树的前序遍历

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left,res)
        self.dfs(root.right,res)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = [root]
        while s:
            node = s.pop()
            if node:
                res.append(node.val)
                s.append(node.right)
                s.append(node.left)
        return res

# 145. 二叉树的后序遍历


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        self.dfs(root.left,res)
        self.dfs(root.right,res)
        res.append(root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = [(root,False)]
        while s:
            node, v = s.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    s.append((node,True))
                    s.append((node.right,False))
                    s.append((node.left,False))
        return res


# MorrisTravel


def MorrisTravel(root):
    node = root
    while node != None:
        if node.left == None:
            print(node.val,end=" ")
            node = node.right
        else:
            pre = getPredecessor(node)
            if pre.right= None:
                pre.right = node
                node = node.left
            elif pre.right == node:
                pre.right = None
                print(node.val,end=" ")
                node = node.right



def getPredecessor(node):
    pre = node
    if node.left != None:
        pre = pre.left
        while pre.right != None and pre.right != node:
            pre= pre.right
    return pre
