# 65. Valid Number

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = re.compile(r'^[+-]?(\d+[.]?|\d*[.]\d+)(e[+-]?\d+)?$')
        if len(s.strip()) == 0:
            return False
        m = p.match(s.strip())
        return m != None


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        if n == 0:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False
        seen_sign = False

        for i,ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in ('e', 'E'):
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            elif ch in ('+','-'):
                if i > 0 and s[i-1] not in ('e','E'):
                    return False
            else:
                return False
        return seen_digit