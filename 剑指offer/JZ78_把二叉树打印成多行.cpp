/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param pRoot TreeNode类
     * @return int整型vector<vector<>>
     */
    vector<vector<int> > Print(TreeNode* pRoot) {
        // write code here
        if (!pRoot) return {};

        queue<TreeNode*> q;
        vector<vector<int>> result ={};

        int level_length = 0;
        int depth = 0;

        q.push(pRoot);

        TreeNode* node;

        while(!q.empty()){
            level_length = q.size();
            result.push_back({});

            for (int i=0;i<level_length;i++){
                node = q.front();
                q.pop();
                result[depth].push_back(node->val);

                if (node->left) q.push(node->left);
                if (node->right)    q.push(node->right);
            }

            depth += 1;
        }

        return result;
    }
};
