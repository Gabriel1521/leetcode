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
     bool isSameTree(TreeNode* p, TreeNode* q) {
         if (!p && !q)
             return true;
         else if (!p || !q)
             return false;
         else if (p->val != q->val)
             return false;
         else
             return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
     }
 };

// Complexity Analysis
// Time complexity : O(N),
// where N is a number of nodes in the tree, since one visits
// each node exactly once.

// Space complexity : O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

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
    bool check(TreeNode* a, TreeNode* b){
        if (!a && !b)
            return true;
        else if (!a || !b)
            return false;
        else if (a->val != b->val)
            return false;
        else
            return true;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<vector<TreeNode*>> que;
        que.push({p,q});
        while (!que.empty()){
            vector<TreeNode*> v = que.front();
            que.pop();
            TreeNode* node_a = v[0];
            TreeNode* node_b = v[1];
            if (!check(node_a, node_b)) return false;
            else{
                if (node_a != nullptr){
                    que.push({node_a->left, node_b->left});
                    que.push({node_a->right, node_b->right});
                }
            }
        }
        return true;
    }
};

// Complexity Analysis

// Time complexity : O(N) since each node is visited
// exactly once.

// Space complexity : O(N) in the worst case, where the tree is a perfect fully balanced binary tree, since BFS will have to store at least an entire level of the tree in the queue, and the last level has O(N)O(N)O(N) nodes.
