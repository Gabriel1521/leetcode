# 3. Longest Substring Without Repeating Characters

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

# 159. Longest Substring with At Most Two Distinct Characters

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = collections.defaultdict(int)
        start, end = 0, 0
        maxlen = -float('inf')
        n = len(s)
        while end < n:
            cur = s[end]
            if len(dic) == 2 and cur not in dic:     # find the third distinct char
                maxlen = max(maxlen, end-start)      # update max length
                pos = min(dic.values())              # find the last position of the first char in current window
                start = pos + 1                      # update window (start from the second char)
                del dic[s[pos]]                      # update dictionary by deleting the first char
            dic[cur] = end                           # update position of current char
            end += 1
        return max(maxlen, n-start)
