class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,3,2,4]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1

        return left
                    