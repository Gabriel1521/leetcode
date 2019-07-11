# 225. Implement Stack using Queues

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.q1 = collections.deque([])
        self.q2 = collections.deque([])


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        while self.q2:
            self.q1.append(self.q2.popleft())

        self.q1.append(x)
        self.count += 1


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.q1:
            if len(self.q1) == 1:
                self.count -= 1
                return self.q1.popleft()
            self.q2.append(self.q1.popleft())
        while self.q2:
            if len(self.q2) == 1:
                self.count -= 1
                return self.q2.popleft()
            self.q1.append(self.q2.popleft())



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q2:
            return self.q2[-1]
        if self.q1:
            return self.q1[-1]



    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.count == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
