/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> result={};
        while (head){
            result.push_back(head->val);
            head = head->next;
        }
        reverse(result.begin(),result.end());
        return result;

    }
};
