class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(k):
            left = 0
            odds = 0
            ans = 0
            for right in range(len(nums)):
                if nums[right] % 2: odds += 1
                while odds > k:
                    if nums[left] % 2: odds -= 1
                    left += 1
                ans += right - left + 1
            return ans
        return helper(k) - helper(k - 1)