
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead) {
        if (pHead == nullptr || pHead->next == nullptr) return pHead;

        ListNode* node = pHead;
        ListNode* head = new ListNode(0);
        head->next = pHead;
        ListNode* prev = head;

        while (node != nullptr){
            if (node->next != nullptr && node->val == node->next->val){
                while (node->next != nullptr && node->val == node->next->val){
                    node = node->next;
                }
                prev->next = node->next;
                node = node->next;
            }
            else{
                prev = prev->next;
                node = node->next;
            }
        }

        return head->next;

    }
};
