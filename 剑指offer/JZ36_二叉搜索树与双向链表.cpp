/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree) {
        TreeNode* first = nullptr;
		TreeNode* last = nullptr;

		TreeNode * node = pRootOfTree;

		stack<TreeNode*> s;

		while (!s.empty() || node){
			while (node){
				s.push(node);
				node = node->left;
			}
			node = s.top();
			s.pop();
			if (first==nullptr){
				first = node;
			}
			else{
				node->left = last;
				last->right = node;
			}
			last = node;
			node = node->right;
		}

		return first;
    }
};
