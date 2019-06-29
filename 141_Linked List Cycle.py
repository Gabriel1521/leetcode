# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if slow is None or fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


# 142. Linked List Cycle II

class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while True:
            if fast == None or fast.next == None: return None
            slow = slow.next; fast = fast.next.next
            if slow == fast: break
        while head != fast:
            head = head.next; fast = fast.next
        return head
