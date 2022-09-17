class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        add = -inf
        ans = -inf
        for i, v in enumerate(values):
            ans = max(ans, add + v - i)
            add = max(add, v + i)
        return ans