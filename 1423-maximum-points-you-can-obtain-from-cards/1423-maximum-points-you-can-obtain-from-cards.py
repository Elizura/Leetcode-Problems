class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        tot_sum = sum(cardPoints)
        if k == N: return tot_sum
        size = N - k
        l, r = 0, size - 1
        pref = sum(cardPoints[l: r])
        max_pts = 0
        while r < N:            
            pref += cardPoints[r]
            max_pts = max(max_pts, tot_sum - pref)
            pref -= cardPoints[l]
            l += 1
            r += 1
        return max_pts