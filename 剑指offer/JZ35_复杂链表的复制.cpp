/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead) {
        if (pHead == nullptr)   return nullptr;

        map<RandomListNode*, RandomListNode*> m;
        RandomListNode* node = pHead;
        RandomListNode* pre;
        RandomListNode* res;

        while (node){
            if (node == pHead){
                m[node] = new RandomListNode(node->label);
                pre = m[node];
                res = m[node];
                node = node->next;
            }
            else{
                m[node] = new RandomListNode(node->label);
                pre->next = m[node];
                pre = pre->next;

                node = node->next;
            }
        }

        for (auto &[key, value]:m){
            if (key->random == nullptr){
                value->random = nullptr;
            }else{
                value->random = m[key->random];
            }
        }

        return res;
    }
};
