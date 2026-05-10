class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        d = dict()
        st = []

        d[')'] = '('
        d[']'] = '['
        d['}'] = '{'

        for i in range(n):
            if s[i] in d.values():
                st.append(s[i])
            elif s[i] in d:
                if len(st) == 0:
                    return False
                tmp = st.pop()
                if d[s[i]] != tmp:
                    return False
        
        return len(st) == 0