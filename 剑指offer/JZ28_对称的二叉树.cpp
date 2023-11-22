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
     * @param pRoot TreeNode类
     * @return bool布尔型
     */
    bool isSymmetrical(TreeNode* pRoot) {
        // write code here
        return symmetric(pRoot, pRoot);
    }

    bool symmetric(TreeNode* a, TreeNode* b){
        if (!a && !b)   return true;
        if ((!a && b) || (!b && a)) return false;
        if (a->val != b->val)   return false;
        return symmetric(a->left, b->right) && symmetric(a->right, b->left);
    }
};
