/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> vec;
        stack<TreeNode*> s;
        TreeNode* cur=root;
        while(cur!=nullptr || !s.empty()) {
            while(cur!=nullptr) {
                s.push(cur);
                cur=cur->left;
            }
            cur=s.top();
            s.pop();
            vec.push_back(cur->val);
            cur=cur->right;
        }
        return vec;
    }

};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        inorder(root, nodes);
        return nodes;
    }
private:
    void inorder(TreeNode* root, vector<int>& nodes) {
        if (!root) {
            return;
        }
        inorder(root -> left, nodes);
        nodes.push_back(root -> val);
        inorder(root -> right, nodes);
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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr){
            return {};
        }
        vector<int> result;
        dfs(root, result);
        return result;
    }

    void dfs(TreeNode* root, vector<int>& result){
        if (root == nullptr){
            return;
        }
        dfs(root->left, result);
        result.push_back(root->val);
        dfs(root->right,result);
    }
};
