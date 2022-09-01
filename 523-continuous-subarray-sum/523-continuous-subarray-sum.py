class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            remainder = pref % k
            if remainder in dic:
                if i - dic[remainder] >= 2: return True             
            else:
                dic[remainder] = i
        return False
        # for i in range(len(nums)):
        #     sem = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         sem += nums[j]
        #         if sem % k == 0: return True
        # return False