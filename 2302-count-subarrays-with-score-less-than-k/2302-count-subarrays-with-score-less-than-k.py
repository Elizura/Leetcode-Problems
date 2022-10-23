class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sum, res, j = 0, 0, 0
        # for i, n in enumerate(nums):
        #     sum += n
        #     while sum * (i - j + 1) >= k:
        #         sum -= nums[j]
        #         j += 1
        #     res += i - j + 1
        # return res
        pref = 0        
        left = 0
        ans = 0
        N = len(nums)
        for right in range(N):
            pref += nums[right]
            while pref*(right - left + 1) >= k:
                pref -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
                
        # while right < N:
            # while right < N and (pref) * (right - left + 1) < k:
            #     pref += nums[right]
            #     right += 1                
            # size = (right - left)
            # ans += (size) * (size + 1) / 2
            # while (pref) * (right - left + 1) >= k:
            #     pref -= nums[left]
            #     left += 1
            # right += 1
                
            