class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:            
            mid = l + (r - l)//2            
            if nums[mid] == target:
                return mid            
            if nums[mid] >= nums[r]:
                if target > nums[mid] or target < nums[l]:
                    l = mid  + 1
                else:
                    r = mid - 1 
            else:
                
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1                    
            # else:
            #     return mid
        return -1
                