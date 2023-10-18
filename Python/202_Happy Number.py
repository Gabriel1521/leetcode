# 202. Happy Number

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        l = []
        count = 0
        mem = set()
        while n != 1:
            s = 0
            l = []
            while n > 0:
                l.append(n%10)
                n = int(n/10)

            for i in range(len(l)):
                s += l[i] * l[i]

            n = s

            if n in mem:
                return False
            else:
                mem.add(n)
        return True
