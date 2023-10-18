# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        l1 = l = ListNode(0)
        r1 = r = ListNode(0)
        while head:
            l.next = head
            r.next = head.next
            l = l.next
            r = r.next
            if r:
                head = head.next.next
            else:
                head = None
        l.next = r1.next
        return l1.next
