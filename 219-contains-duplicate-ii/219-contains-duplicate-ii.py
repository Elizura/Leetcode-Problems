class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for idx, val in enumerate(nums):
            if val in dic and abs(dic[val] - idx) <= k: return True
            dic[val] = idx
        return False