class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i
                
                
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]