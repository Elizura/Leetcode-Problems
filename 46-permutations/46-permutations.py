class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        mask = 0
        # included = set()
        per = []
        def backtracking(mask):            
            if len(per) == len(nums):                
                ans.append(per[:])
                return             
            for i in range(len(nums)):                
                # if nums[i] in included: continue
                if mask & 1<<i: continue
                # included.add(nums[i])                
                mask |= 1<<i                
                per.append(nums[i]) 
                backtracking(mask)           
                # included.remove(nums[i])
                mask -= 1 << i
                per.remove(nums[i])
        backtracking(mask)
        return ans