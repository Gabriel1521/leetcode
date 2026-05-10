class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        
        

    def pop(self):
        """
        :rtype: None
        """
        return self.s.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        top = self.s[-1]
        return top


    def getMin(self):
        """
        :rtype: int
        """
        mn = min(self.s)
        return mn