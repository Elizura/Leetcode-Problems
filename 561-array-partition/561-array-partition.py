class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        for i in range(0, len(nums) - 1, 2):
            temp.append((nums[i], nums[i + 1]))
        ans = 0
        print(temp)
        for i in temp:
            ans += min(i[0], i[1])
        return ans