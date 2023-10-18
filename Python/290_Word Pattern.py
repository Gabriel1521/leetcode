# 290. Word Pattern

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(' ')

        if len(pattern) != len(l):
            return False
        if len(set(pattern)) != len(set(l)):
            return False
        l1 = len(pattern)
        d = dict()
        for i in range(l1):
            if pattern[i] not in d:
                d[pattern[i]] = l[i]

        for i in range(l1):
            if l[i] != d[pattern[i]]:
                return False

        return True


# 291. Word Pattern II

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, s, d):
        if len(pattern) == 0 and len(s) > 0:
            return False
        if len(pattern) == len(s) == 0:
            return True
        for i in range(1,len(s)+1):
            if pattern[0] not in d and s[:i] not in d.values():
                d[pattern[0]] = s[:i]
                if self.dfs(pattern[1:], s[i:], d):
                    return True
                del d[pattern[0]]
            elif pattern[0] in d and d[pattern[0]] == s[:i]:
                if self.dfs(pattern[1:], s[i:], d):
                    return True
        return False
