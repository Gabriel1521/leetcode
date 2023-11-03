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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root==nullptr){
            return {};
        }
        deque<TreeNode*> l;
        vector<vector<int>> result;
        int level=0;
        int n;
        TreeNode* node = root;
        bool s= true;
        l.push_back(node);
        while (l.size()!=0){
            n = l.size();
            deque<int> level_l = {};
            for (int i=0;i<n;i++){
                node = l.front();
                l.pop_front();
                if (s==true){
                    level_l.push_back(node->val);
                }else{
                    level_l.push_front(node->val);
                }

                if (node->left!=nullptr){
                        l.push_back(node->left);
                }
                if (node->right!=nullptr){
                        l.push_back(node->right);
                }

            }
            if (s==true){
                        s=false;
            }
            else{
                        s=true;
            }
            result.push_back({});
            for (auto& element:level_l){
                result[level].push_back(element);
            }
            level += 1;
        }
        return result;

    }
};
