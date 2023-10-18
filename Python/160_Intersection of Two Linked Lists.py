# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None

        d = dict()
        while headA:
            d[headA] = 1
            headA = headA.next

        while headB:
            if headB in d:
                break
            headB = headB.next

        if headB in d:
            return headB
        else:
            return None
