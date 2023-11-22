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
     * @return TreeNode类
     */
    TreeNode* Mirror(TreeNode* pRoot) {
        // write code here
        if (!pRoot) return nullptr;
        TreeNode* left = Mirror(pRoot->right);
        TreeNode* right = Mirror(pRoot->left);
        pRoot->left = left;
        pRoot->right = right;
        return pRoot;
    }
};


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
     * @return TreeNode类
     */
    TreeNode* Mirror(TreeNode* pRoot) {
        // write code here
        if (!pRoot) return nullptr;
        queue<TreeNode*> q;
        q.push(pRoot);
        while (!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            TreeNode* left = node->right;
            TreeNode* right = node->left;
            node->left = left;
            node->right = right;
            if (node->left) q.push(node->left);
            if (node->right)    q.push(node->right);
        }
        return pRoot;
    }
};
