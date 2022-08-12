class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen =  set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return i
        