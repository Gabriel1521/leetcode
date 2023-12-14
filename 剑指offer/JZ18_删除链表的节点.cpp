/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param head ListNode类
     * @param val int整型
     * @return ListNode类
     */
    ListNode* deleteNode(ListNode* head, int val) {
        // write code here
        ListNode* res = new ListNode(0);
        ListNode* node = head;
        res->next = node;
        ListNode* prev = res;

        while (node){
            if (node->val == val){
                prev->next = node->next;
                node = node->next;
            }
            else{
                prev = prev->next;
                node = node->next;
            }
        }
        return res->next;
    }
};
