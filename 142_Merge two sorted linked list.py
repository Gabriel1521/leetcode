# 142.Merge two sorted linked list

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            dummyNode = cur = ListNode(0)

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next

                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next


            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummyNode.next
