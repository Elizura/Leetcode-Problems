class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:        
        nums.sort()
        N = len(nums)
        if N == 1:
            return nums
        ans = []        
        for i in range(N):
            if i == 0:
                if nums[i + 1] != nums[i] and nums[i + 1] != nums[i] + 1:
                    ans.append(nums[i])
            elif i == N - 1:
                if nums[i - 1] != nums[i] and nums[i - 1] != nums[i] - 1:
                    ans.append(nums[i])
            elif nums[i - 1] != nums[i] - 1 and nums[i + 1] != nums[i] + 1 and nums[i - 1] != nums[i] and nums[i + 1] != nums[i]:                
                ans.append(nums[i])
        return ans