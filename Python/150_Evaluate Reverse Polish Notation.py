from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                b = s.pop()
                a = s.pop()
                if token == "+":
                    res = a+b
                elif token == "-":
                    res = a-b
                elif token == "*":
                    res = a*b
                else:
                    res = int(a/b)
                s.append(res)
            else:
                s.append(int(token))
        return s[0]