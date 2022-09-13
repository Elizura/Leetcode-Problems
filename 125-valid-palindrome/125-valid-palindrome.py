class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in s:
            if i.isalnum():
                new += i.lower()
        l, r = 0, len(new) - 1
        while r >= l:
            if new[l] != new[r]: return False
            l += 1
            r -= 1
        return True