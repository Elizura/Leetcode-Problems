class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  #O(n)
        while len(nums) > k:  #O(1)
            heapq.heappop(nums) 
            
        return nums[0]