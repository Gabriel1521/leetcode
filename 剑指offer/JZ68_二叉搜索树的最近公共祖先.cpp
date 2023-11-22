/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param root TreeNode类
     * @param p int整型
     * @param q int整型
     * @return int整型
     */

    TreeNode* dfs(TreeNode* root, int p, int q){
        if (!root)  return nullptr;
        if (root->val == p|| root->val==q)  return root;
        if (p < root->val && q < root->val) return dfs(root->left, p, q);
        if (p > root->val && q > root->val) return dfs(root->right, p, q);
        return root;
    }

    int lowestCommonAncestor(TreeNode* root, int p, int q) {
        // write code here
        TreeNode* result = dfs(root, p, q);
        return result->val;
    }
};
