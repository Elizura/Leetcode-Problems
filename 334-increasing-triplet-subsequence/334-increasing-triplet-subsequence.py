class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        #O(n) time and O(1) space
        _min = nums[0]
        _max = inf
        for i in nums[1:]:
            if i > _max:
                return True
            elif i < _min:
                _min = i
            elif i > _min and i < _max:
                _max = i
        return False
                
        
        #O(n) time and O(n) space
        
#         _min = [nums[0]]
#         _max = [nums[-1] for i in range(len(nums))]
        
#         for i in range(1, len(nums)):
#             if nums[i] < _min[-1]:
#                 _min.append(nums[i])
#             else:
#                 _min.append(_min[-1])
                
#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] > _max[i + 1]:
#                 _max[i] = nums[i]
#             else:
#                 _max[i] = _max[i + 1]
                
#         for i in range(len(nums)):
#             if _min[i] < nums[i] < _max[i]:
#                 return True        
#         return False
                
        # tab = [1 for i in range(len(nums))]
        # for i in range(1, len(tab)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             tab[i] = max(tab[i], tab[j] + 1)
        #         if tab[i] >= 3: return True
        # return False