class Solution:
    def firstfinder(nums, target):
        l, r, first_index = 0, len(nums) - 1, -1
        while l <= r:
            m = l + (r - l)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                first_index = m
                r = m - 1
            else:
                l = m + 1
        return first_index
    def lastfinder(nums, target):
        l, r, last_index = 0, len(nums) - 1, -1
        while l <= r:
            m = l + (r - l)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                last_index = m
                l = m + 1
            else:
                l = m + 1
        return last_index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums :
#             return [-1, -1]
#         start_ind, end_ind = -1, -1
#         a = bisect.bisect_left(nums, target)
#         b = bisect.bisect_right(nums, target)
        
#         if a < len(nums) and nums[a] == target: start_ind = a
#         if nums[b - 1] == target: end_ind = b - 1
#         return [start_ind, end_ind]
        a = Solution.firstfinder(nums, target)
        b = Solution.lastfinder(nums, target)
        return [a,b]
    