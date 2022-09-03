class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # ans = inf
        # arr = [0 for i in range(len(nums) + 1)]
        # arr[0] = 0
        # for i in range(1, len(arr)):
        #     arr[i] = arr[i - 1]  + nums[i - 1]
        # l, r = 0, len(arr) - 1
        # for i in range(len(arr)):
        #     while r >= l:
        #         mid = l + (r - l) // 2
        #         cur = arr[mid] - arr[i]
        #         if cur < target:
        #             l = mid + 1                    
        #         else:
        #             ans = min(ans, mid - (i - 1))
        #             r = mid - 1
        # return ans
        ans = inf
        sun = 0
        l, r = 0, 0
        while r <= len(nums) and r >= l:            
            if sun < target:
                if r == len(nums): break
                sun += nums[r]
                r += 1
            else:
                ans = min(ans, r - l)
                sun -= nums[l]                
                l += 1
                
        return 0 if ans is inf else ans

