class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        dic = {}
        good = 0
        N = len(nums)
        for idx, num in enumerate(nums):
            difference = idx - num
            if difference in dic:
                good += dic[difference]
                dic[difference] += 1
            else:
                dic[difference] = 1
        return int((N*(N - 1)/2) - good)

        
        # return tot - good
        # ans = 0
        # N = len(nums)
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         if j - i != nums[j] - nums[i]:
        #             ans += 1
        # return ans