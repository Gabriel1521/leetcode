# 392. Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        idx = 0
        d = dict()
        for i in range(n):
            if s[i] not in t[idx:]:
                return False
            if s[i] not in d:
                idx = t.index(s[i])
                d[s[i]] = idx
                idx += 1
            else:
                prev = d[s[i]]
                idx = max(prev+1,idx)
                if s[i] not in t[idx:]:
                    return False
                d[s[i]] = t[idx:].index(s[i])+prev+1

        return True
