class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        pref = list(accumulate(arr))
        N = len(arr)
        ans = 0
        for i in range(N - k + 1):
            left = i
            right = i + k - 1
            tot = pref[right] - pref[left] + arr[left]
            length = right - left + 1
            avg = tot/length
            if avg >= threshold:                
                ans += 1
        return ans
    