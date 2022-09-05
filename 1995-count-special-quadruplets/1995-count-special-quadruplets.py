class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        #very much brute force O(n^4)
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[l] == nums[i] + nums[k] + nums[j]:
                            ans += 1
        return ans