class Solution:
    def canPartition(self, nums: List[int]) -> bool:                
        sem = sum(nums)
        target = sem/2
        if int(target) != target: return False
        a = [False for i in range(int(target) + 1)]
        a[0] = True
        for num in nums:
            for i in range(len(a) -1, num - 1, -1):
                a[i] = a[i] or a[i - num]        
        return a[-1]
        # seen = set([0])
        # sem = sum(nums)
        # target = sem/2
        # if int(target) != target: return False        
        # def dfs(index, aim, memo = {}):
        #     if (index, aim) in memo: return memo[(index, aim)]
        #     if index >= len(nums): return False
        #     if aim == 0: return True
        #     memo[(index, aim)] = dfs(index + 1, aim - nums[index]) or dfs(index + 1, aim) 
            # return memo[(index, aim)]
        # return dfs(0, target)
        # seen = set([0])
        # sem = sum(nums)
        # target = sem/2
        # if int(target) != target: return False
        # for i in range(len(nums) - 1, -1, -1):
        #     temp = set()
        #     # temp = seen
        #     for j in seen:               
        #         temp.add(j + nums[i])
        #         temp.add(j)
        #     seen = temp
        # if target in seen: return True
        # return False