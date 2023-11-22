/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <numeric>
#include <algorithm>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param root TreeNode类
     * @param sum int整型
     * @return int整型
     */
    int path_count=0;
    void dfs(TreeNode* root, int sum){
        if (!root)  return;
        sum -= root->val;
        if (sum==0) path_count += 1;
        dfs(root->left, sum);
        dfs(root->right, sum);
        return;
    }


    int FindPath(TreeNode* root, int sum) {
        // write code here
        if (!root)  return 0;

        dfs(root, sum);
        FindPath(root->left, sum);
        FindPath(root->right, sum);

        return path_count;

    }
};
