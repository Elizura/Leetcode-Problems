class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(1, len(s)):
            if int(s[i]) == 0 and '1' in s[i:]:                                   
                return False
        return True