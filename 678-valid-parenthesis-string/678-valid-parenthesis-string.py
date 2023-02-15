class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i, c in enumerate(s):
            if c == '(':
                s1.append(i)
            elif c == '*':
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False

        while s1 and s2:
            if s1[-1] > s2[-1]: # ( is closer to the end than *
                return False
            s1.pop()
            s2.pop()
        return s1 == []