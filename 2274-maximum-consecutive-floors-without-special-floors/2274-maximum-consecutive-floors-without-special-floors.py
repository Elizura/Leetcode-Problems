class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        for i in range(1, len(special)):
            floors = special[i] - special[i - 1] - 1
            ans = max(ans, floors)
        return max(ans, special[0] - bottom, top - special[-1] )
            
        # ans = 0
        # temp = 0
        # special_ = set()
        # for i in special:
        #     special_.add(i)
        # for i in range(bottom, top + 1):
        #     if i not in special_ :
        #         temp += 1
        #         ans = max(ans, temp)
        #     else:
        #         temp = 0
        # return ans