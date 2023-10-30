

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root==nullptr){
            return {};
        }
        deque<TreeNode*> q;
        vector<vector<int>> result;
        int level=0;
        int l;
        TreeNode* node = root;
        q.push_back(node);
        while (!q.empty()){
            l = q.size();
            result.push_back({});
            for (int i=0;i<l;i++){
                node = q.front();
                q.pop_front();
                result[level].push_back(node->val);
                if (node->left != nullptr){
                    q.push_back(node->left);
                }
                if (node->right != nullptr){
                    q.push_back(node->right);
                }
            }
            level += 1;

        }

        return result;
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr){
            return {};
        }
        queue<TreeNode*> q;
        vector<vector<int>> result;
        TreeNode* node = root;
        q.push(node);
        int level = 0;
        int l;
        while (!q.empty()){
            l = q.size();
            result.push_back({});
            for (int i=0;i<l;i++){
                node = q.front();
                q.pop();
                result[level].push_back(node->val);
                if (node->left != nullptr){
                    q.push(node->left);
                }
                if (node->right != nullptr){
                    q.push(node->right);
                }

            }
            level += 1;

        }
        return result;

    }
};
