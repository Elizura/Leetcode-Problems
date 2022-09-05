class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = [set(i) for i in nums]
        temp = seen[0]        
        ans = []
        for i in range(len(nums)):
            temp = temp & seen[i]
        for i in temp:
            ans.append(i)
        ans.sort()
        return ans