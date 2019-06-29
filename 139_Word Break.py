# 139. Word Break

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

# 140. Word Break II

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict.sort()
        res = []
        self.dfs(s, wordDict, "", res)
        return res

    def dfs(self, s, wordDict, path, res):
        if self.check(s, wordDict):
            if not s and path not in res:
                res.append(path[:-1])
                return
            for i in range(len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict,path+s[:i]+" ",res)

    def check(self, s, dic):
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]
