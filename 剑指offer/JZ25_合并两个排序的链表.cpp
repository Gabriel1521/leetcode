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
     * @param pHead1 ListNode类
     * @param pHead2 ListNode类
     * @return ListNode类
     */
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
        // write code here
        if (!pHead1)    return pHead2;
        if (!pHead2)    return pHead1;

        if (pHead1->val < pHead2->val){
            pHead1->next = Merge(pHead1->next, pHead2);
            return pHead1;
        }else{
            pHead2->next = Merge(pHead1, pHead2->next);
            return pHead2;
        }


    }
};

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
     * @param pHead1 ListNode类
     * @param pHead2 ListNode类
     * @return ListNode类
     */
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
        // write code here
        ListNode* dummy = new ListNode(0);
        ListNode* node = dummy;

        while (pHead1 && pHead2){
            if (pHead1->val < pHead2->val){
                node->next = pHead1;
                pHead1 = pHead1->next;
            }
            else{
                node->next = pHead2;
                pHead2 = pHead2->next;
            }
            node = node->next;
        }

        if (pHead1) node->next = pHead1;
        if (pHead2) node->next = pHead2;

        return dummy->next;

    }
};

// Time Complexity: O(m+n)
// Space Complexity: O(1)
