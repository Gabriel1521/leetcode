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
    bool _isSymmetric(TreeNode* a, TreeNode* b){
        if (!a && !b)   return true;
        if (!a || !b)   return false;
        if (a->val != b->val)   return false;
        else    return (a->val == b->val) && _isSymmetric(a->left,b->right) && _isSymmetric(a->right, b->left);
    }

    bool isSymmetric(TreeNode* root) {
        return _isSymmetric(root, root);
    }
};

// Complexity Analysis

// Time complexity : O(n). Because we traverse the entire input tree once, the total run time is O(n), where nnn is the total number of nodes in the tree.

// Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.

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
    bool isSymmetric(TreeNode* root){
        queue<TreeNode*> q;
        q.push(root);
        q.push(root);
        while (!q.empty()){
            TreeNode* n1 = q.front();
            q.pop();
            TreeNode* n2 = q.front();
            q.pop();
            if (!n1 && !n2) return true;
            if (!n1 || !n2) return false;
            if (n1->val != n2->val) return false;
            if (n1->left){
                q.push(n1->left);
                q.push(n2->right);
            }
            if (n1->right){
                q.push(n1->right);
                q.push(n2->left);
            }
        }
        return true;
    }
};

//Complexity Analysis

// Time complexity : O(n)O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n)O(n), where nnn is the total number of nodes in the tree.

// Space complexity : There is additional space required for the search queue. In the worst case, we have to insert O(n)O(n)O(n) nodes in the queue. Therefore, space complexity is O(n)O(n)O(n).
