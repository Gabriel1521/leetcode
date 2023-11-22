/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* node, int depth, int& maxdepth){
        if(!node)   return;
        if (!node->left && !node->right){
            if (depth > maxdepth)
                maxdepth = depth;
                return;
        }
        dfs(node->left, depth+1, maxdepth);
        dfs(node->right, depth+1, maxdepth);
    }
    int maxDepth(TreeNode* root) {
        int maxdepth = 0;
        dfs(root, 1, maxdepth);
        return maxdepth;
    }
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root)  return 0;
        return max(1 + maxDepth(root->left), 1 + maxDepth(root->right));
    }
};
