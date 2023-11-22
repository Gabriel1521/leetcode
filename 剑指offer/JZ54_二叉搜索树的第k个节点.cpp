/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <type_traits>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param proot TreeNode类
     * @param k int整型
     * @return int整型
     */
    int KthNode(TreeNode* proot, int k) {
        if (!proot) return -1;
        // write code here
        vector<int> result = {};
        dfs(proot, result);
        if (k > result.size() || k<1)  return -1;
        return result[k-1];
    }

    void dfs(TreeNode* node, vector<int>& result){
        if (!node)  return;
        dfs(node->left, result);
        result.push_back(node->val);
        dfs(node->right, result);
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
#include <type_traits>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param proot TreeNode类
     * @param k int整型
     * @return int整型
     */
    int KthNode(TreeNode* proot, int k) {
        // write code here
        if (!proot || k < 1)
            return -1;

        stack<TreeNode*> s;
        TreeNode* node = proot;

        while (node || !s.empty()){
            while (node){
                s.push(node);
                node = node->left;
            }
            node = s.top();
            s.pop();

            k -= 1;
            if (k==0)   return node->val;

            node = node->right;

        }

        return -1;
    }
};
