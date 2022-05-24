class Solution:
    def isValid(self, s: str) -> bool:
        b=[]
        a={')':'(',
           '}':'{',
           ']':'['}
        for i in s:
            if i in a.values():
                b.append(i)
            if i in a.keys():
                if b and b[-1]==a[i]:
                    b.pop()
                else:
                    return False
        return False if b else True
                    