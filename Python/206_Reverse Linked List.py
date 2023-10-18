
# 206 Reverse Linked List

def reverselist(self,head):
  prev = None
  temp = head
  while temp:
    cur = temp
    temp = temp.next
    cur.next = prev
    prev = cur
  return prev

2. Reverse Linked List II

def reverseBetween(self,head,m,n):
  if m == n:
    return head

  dummyNode = ListNode(0)
  dummyNode.next = head
  prev = dummyNode

  for i in range(m-1):
      prev = prev.next

  reverse = None
  cur = prev.next
  for i in range(n-m+1):
      next = cur.next
      cur.next = reverse
      reverse = cur
      cur = next

  prev.next.next = cur
  prev.next = reverse
  return dummyNode.next


3.Reverse Doubly Linked List

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class Doubly Linked List:
  def __init__(self):
    self.head = None

  def reverse(self):
    temp = None
    current = self.head

    while current is not None:
      temp = current.prev
      current.prev = current.next
      current.next = temp
      current = current.prev

    if temp is not None:
      self.head = temp.prev

# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head

# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
