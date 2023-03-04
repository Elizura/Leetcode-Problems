class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:        
        N = len(nums)
        ans = [-1]*N
        pref = list(accumulate(nums))
        for i in range(k, N - k):
            left = i - k
            right = i + k
            length = right - left + 1
            tot = pref[right] - pref[left] + nums[left]
            ans[i] = tot//length            
        return ans