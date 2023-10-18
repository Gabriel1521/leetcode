# 394. Decode String

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(["",int(num)])
                num = ""
            elif ch == "]":
                st, k = stack.pop()
                stack[-1][0] += k*st
            else:
                stack[-1][0] += ch
        return stack[0][0]