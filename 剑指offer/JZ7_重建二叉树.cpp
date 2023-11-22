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
     * @param preOrder int整型vector
     * @param vinOrder int整型vector
     * @return TreeNode类
     */
    TreeNode* reConstructBinaryTree(vector<int>& preOrder, vector<int>& vinOrder) {
        // write code here
        if (preOrder.empty())   return nullptr;

        TreeNode* root = new TreeNode(preOrder[0]);

        vector<int>::iterator it;
        it = find(vinOrder.begin(), vinOrder.end(), preOrder[0]);
        int idx = it - vinOrder.begin();

        vector<int> preOrder_left = vector<int>(preOrder.begin()+1,preOrder.begin()+idx+1);
        vector<int> preOrder_right = vector<int>(preOrder.begin()+idx+1,preOrder.end());

        vector<int> vinOrder_left = vector<int>(vinOrder.begin(),vinOrder.begin()+idx);
        vector<int> vinOrder_right = vector<int>(vinOrder.begin()+idx+1, vinOrder.end());

        root->left = reConstructBinaryTree(preOrder_left, vinOrder_left);
        root->right = reConstructBinaryTree(preOrder_right, vinOrder_right);

        return root;
    }
};
