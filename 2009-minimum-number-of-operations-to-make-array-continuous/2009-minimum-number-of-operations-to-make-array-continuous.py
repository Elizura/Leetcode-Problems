class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(set(nums))
        operations = inf
        for start in range(len(nums)):
            end = N + nums[start] - 1
            idx = bisect_right(nums, end)
            operations = min(operations, N - (idx - start))
        return operations