/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {

    }
};
*/
class Solution {
public:
    vector<TreeLinkNode*> nodes={};

    void dfs(TreeLinkNode* root){
        if (!root)  return;
        dfs(root->left);
        nodes.push_back(root);
        dfs(root->right);
    }

    TreeLinkNode* GetNext(TreeLinkNode* pNode) {
        TreeLinkNode* root = pNode;
        while (root->next)  root = root->next;

        dfs(root);

        int n = nodes.size();
        for (int i=0;i<n;i++){
            if (nodes[i] == pNode){
                return nodes[i+1];
            }
        }

        return nullptr;
    }

};
