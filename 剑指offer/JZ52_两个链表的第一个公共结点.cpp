/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        ListNode* ta = pHead1;
		ListNode* tb = pHead2;
		while (ta != tb){
			if (ta != nullptr){
				ta = ta->next;
			}
			else{
				ta = pHead2;
			}
			if (tb != nullptr){
				tb = tb->next;
			}
			else{
				tb = pHead1;
			}
		}
		return ta;
    }
};

/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        ListNode* ta = pHead1;
		ListNode* tb = pHead2;
		while (ta != tb){
			ta = ta? ta->next : pHead2;
			tb = tb? tb->next : pHead1;
		}
		return ta;
    }
};

/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        unordered_set<ListNode*> s1;

		while (pHead1){
			s1.insert(pHead1);
			pHead1 = pHead1->next;
		}

		while (pHead2){
			if (s1.find(pHead2) != s1.end()){
				return pHead2;
			}else{
				pHead2 = pHead2->next;
			}
		}

		return nullptr;
    }
};
