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
    bool isValidBST(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode* node = root;
        while (!s.empty() || node != nullptr){
            while (node != nullptr){
                s.push(node);
                node = node->left;
            }
            node = s.top();
            s.pop();
            result.push_back(node->val);
            node = node->right;
        }

        int l = result.size();

        for (int i=1;i<l;i++){
            if (result[i] < result[i-1] || result[i] == result[i-1]){
                return false;
            }
        }
        return true;

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
    bool isValidBST(TreeNode* root) {
        return validateTree(root, nullptr, nullptr);
    }

    bool validateTree(TreeNode* root, TreeNode* low, TreeNode* high){
        if (root == nullptr){
            return true;
        }

        if ((low != nullptr && root->val <= low->val) || (high != nullptr && high->val <= root->val)){
            return false;
        }

        return validateTree(root->left, low, root) and validateTree(root->right, root, high);
    }
};
