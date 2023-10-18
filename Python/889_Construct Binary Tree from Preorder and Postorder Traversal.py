
# 889. Construct Binary Tree from Preorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if pre:
            root = TreeNode(pre.pop(0))
            post.pop()
            if pre:
                if pre[0] == post[-1]:
                    root.left = self.constructFromPrePost(pre, post)
                else:
                    l, r = post.index(pre[0]), pre.index(post[-1])
                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])
                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:])
            return root

# 105. 从前序与中序遍历序列构造二叉树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None

        val = preorder[0]
        root = TreeNode(val)
        inidx = inorder.index(val)
        left = self.buildTree(preorder[1:inidx+1],inorder[:inidx])
        right = self.buildTree(preorder[inidx+1:],inorder[inidx+1:])
        root.left = left
        root.right = right
        return root
