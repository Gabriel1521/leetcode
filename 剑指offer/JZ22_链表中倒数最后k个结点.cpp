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
     * @param pHead ListNode类
     * @param k int整型
     * @return ListNode类
     */
    ListNode* FindKthToTail(ListNode* pHead, int k) {
        // write code here
        if (pHead==nullptr) return nullptr;

        map<int, ListNode*> m;
        int i = 0;
        ListNode* node = pHead;

        while (node){
            m[i] = node;
            node = node->next;
            i += 1;
        }

        if (k<=i){
            int ans = i-k;
            return m[ans];
        }

        return nullptr;

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
     * @param pHead ListNode类
     * @param k int整型
     * @return ListNode类
     */
    ListNode* FindKthToTail(ListNode* pHead, int k) {
        // write code here
        if (pHead == nullptr)   return nullptr;
        ListNode* node = pHead;
        int n = 0;

        while (node){
            node = node->next;
            n += 1;
        }

        if (k>n || k <= 0){
            return nullptr;
        }

        int ans = n-k;
        int i = 0;

        node = pHead;
        while (i != ans){
            node = node->next;
            i += 1;
        }

        return node;

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
     * @param pHead ListNode类
     * @param k int整型
     * @return ListNode类
     */
    ListNode* FindKthToTail(ListNode* pHead, int k) {
        // write code here
        ListNode* fast = pHead;
        ListNode* slow = pHead;

        for (int i=0;i<k;i++){
            if (fast != nullptr){
                fast = fast->next;
            }else{
                return nullptr;
            }
        }

        while (fast != nullptr){
            fast = fast->next;
            slow = slow->next;
        }

        return slow;
    }
};
