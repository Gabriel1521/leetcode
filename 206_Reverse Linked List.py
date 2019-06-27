
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
