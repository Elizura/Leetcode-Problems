class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):            
            left = 0
            N = len(nums)            
            subarrayCnts = 0
            numsCnt = {}
            for right in range(N):
                numsCnt[nums[right]] = numsCnt.get(nums[right], 0) + 1
                while len(numsCnt) > k:
                    numsCnt[nums[left]] -= 1
                    if not numsCnt[nums[left]]:
                        del numsCnt[nums[left]]
                    left += 1   
                subarrayCnts += right - left + 1                     
            return subarrayCnts
        
        return helper(nums, k) - helper(nums, k - 1)
        