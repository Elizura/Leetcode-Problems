class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        n = len(nums)
        if k % 2 == 1 and n == 1:
            return -1
        if k == n:
            return max(nums[:n-1])
        elif k > n:
            return max(nums)
        else:
            return max(nums[:k-1] + nums[k:k+1])