# 232. Implement Queue using Stacks


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)
        self.count += 1


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return -1
        while self.s1:
            self.s2.append(self.s1.pop())
        self.count -= 1
        return self.s2.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s1: #1234
            return self.s1[0]
        if self.s2: #4321
            return self.s2[-1]



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.count == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
