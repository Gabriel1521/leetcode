#61_Rotate List

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:
            return None

        l = []
        while head:
            l.append(head)
            head = head.next

        if len(l) == 1:
            return l[0]

        n = len(l)

        i = (0-k)%n
        if i != 0:
            l[n-1].next = l[0]
            l[i-1].next = None
        h1 = l[i]
        return h1
