class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        subseq = {i:0 for i in list(set(nums))}
        for i, v in enumerate(nums):
            if count[v] == 0: continue
            count[v] -= 1
            if (v - 1) in subseq and subseq[v - 1] != 0:
                subseq[v - 1] -= 1
                subseq[v] += 1
            else:
                if v + 1 in count and count[v + 1] != 0:
                    if v + 2 in count and count[v + 2] != 0:
                        subseq[v + 2] += 1
                        count[v + 1] -= 1
                        count[v + 2] -= 1
                    else: return False
                else: return False   
        return True
        
        # temp = list(set(nums))
        # count = {}
        # for i in nums:
        #     count[i] = count.get(i, 0) + 1        
        # count = 0
        # for i in range(len(temp)):
        #     if temp[i] != temp[i - 1] and count < k: return False
        #     if count[i] == 0: continue
            