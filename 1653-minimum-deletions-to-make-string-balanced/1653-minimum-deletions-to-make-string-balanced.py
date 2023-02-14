class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans