
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()){
            return nullptr;
        }
        int m = lists.size();
        priority_queue<int, vector<int>, greater<int>> pq;

        for (auto& l : lists){
            while (l){
                pq.push(l->val);
                std::cout << l->val;
                l = l->next;
            }
        }

        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;

        while (!pq.empty()){
            int node_val = pq.top();
            pq.pop();
            cur->next = new ListNode(node_val);
            cur = cur->next;
        }

        return dummy->next;
    }
};
