
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
    ListNode* hasCycle(ListNode* head){
        if (head == nullptr)    return nullptr;
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next != nullptr && fast->next->next !=nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast){
                return slow;
            }
        }

        return nullptr;
    }
    ListNode* EntryNodeOfLoop(ListNode* pHead) {
        ListNode* slow = hasCycle(pHead);

        if (slow == nullptr)
            return nullptr;

        ListNode* fast = pHead;

        while (slow != fast){
            slow = slow->next;
            fast = fast->next;
        }

        return slow;

    }
};


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
    ListNode* EntryNodeOfLoop(ListNode* pHead) {
        if (pHead == nullptr)   return nullptr;

        unordered_set<ListNode*> s;
        ListNode* node = pHead;

        while (node != nullptr){
            if (s.count(node)){
                return node;
            }
            s.insert(node);
            node = node->next;
        }

        return nullptr;
    }
};
