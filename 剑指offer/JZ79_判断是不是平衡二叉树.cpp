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
    bool IsBalanced_Solution(TreeNode* pRoot) {
        // write code here
        if (!pRoot) return true;

        int left = getHeight(pRoot->left);
        int right = getHeight(pRoot->right);
        int diff = abs(left-right);
        return IsBalanced_Solution(pRoot->left) && IsBalanced_Solution(pRoot->right) && diff <=1;
    }

    int getHeight(TreeNode* root){
        if (!root)  return 0;
        return 1 + max(getHeight(root->left),getHeight(root->right));
    }
};
