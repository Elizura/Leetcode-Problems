class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:        
        ans = 1
        pt = 1
        N = len(nums)
        if N == 1: return 1
        for i in range(N):            
            if i + 1 < N:
                if nums[i + 1] > nums[i]:
                    pt = 1
                elif nums[i + 1] == nums[i]:
                    continue
                else:
                    pt = 0
            long = 1            
            for j in range(i + 1, N):                
                if pt and nums[j] > nums[j - 1]:
                    long += 1
                    pt = not pt
                elif not pt and nums[j] < nums[j - 1]:
                    long += 1
                    pt = not pt
            ans = max(ans, long)
        return ans