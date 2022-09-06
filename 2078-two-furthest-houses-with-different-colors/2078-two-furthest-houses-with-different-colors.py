class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i in range(1, len(colors)):
            for j in range(i):
                if colors[i] != colors[j]:
                    dis = i - j
                    ans = max(ans, dis)
        return ans