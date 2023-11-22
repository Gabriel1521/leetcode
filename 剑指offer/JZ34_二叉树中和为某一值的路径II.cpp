/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <numeric>;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param root TreeNode类
     * @param target int整型
     * @return int整型vector<vector<>>
     */
    vector<vector<int> > FindPath(TreeNode* root, int target) {
        // write code here
        if (!root)  return {};
        vector<vector<int>> result = {};
        vector<int> initial_path = {};
        findPath(root, initial_path, result, target);
        return result;
    }

    void findPath(TreeNode* root, vector<int> path, vector<vector<int>>& result, int target){
        if (!root)  return;
        path.push_back(root->val);

        if (!root->left && !root->right){
            int vector_sum = std::accumulate(path.begin(),path.end(),0);
            if (vector_sum == target)   result.push_back(path);
            return;
        }
        findPath(root->left, path, result, target);
        findPath(root->right, path, result, target);
    }
};
