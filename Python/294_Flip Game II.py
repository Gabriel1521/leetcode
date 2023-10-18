# 294. Flip Game II


# 294. Flip Game II

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.memo={}
        return self.helper(s)

    def helper(self,s):
        if s in self.memo:
            return self.memo[s]

        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+' and not self.helper(s[:i]+'--'+s[i+2:]):
                self.memo[s]=True
                return True
        self.memo[s]=False
        return False
