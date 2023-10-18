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
