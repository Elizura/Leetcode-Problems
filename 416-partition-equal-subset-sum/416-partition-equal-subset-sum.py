class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        seen = set([0])
        sem = sum(nums)
        target = sem/2
        if int(target) != target: return False
        for i in range(len(nums) - 1, -1, -1):
            temp = set()
            # temp = seen
            for j in seen:               
                temp.add(j + nums[i])
                temp.add(j)
            seen = temp
        if target in seen: return True
        return False