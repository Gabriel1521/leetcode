# 96. Unique Binary Search Trees

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)

        dp[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[n]

# 95. Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)

                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    if l:
                        print(l.val)
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)


            return all_trees

        return generate_trees(1, n) if n else []
