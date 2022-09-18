class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # if k == 1: return True
        # if len(nums) % k: return
        # count = collections.Counter(nums)
        # for i in range(len(nums)):
        #     prev = nums[i]
        #     if prev == 0: continue
        #     temp = [prev]
        #     for j in range(1, k + 1):
        #         if count[prev] == 0: break
        #         if nums[j] != nums[j - 1] or count[j] == 0: return False
        #         temp.append(nums[i])
        #         count[nums[i]] -= 1
        #     if len(temp) != k and len(nums) != 0: return False            
        # return True
    
        N = len(nums)
        if N % k != 0:
            return False
        
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1                        
        
        while d:
            mn = min(d.keys())
            for i in range(k):
                if (mn+i) in d:
                    if d[(mn+i)] == 1:
                        del d[(mn+i)]
                    else:
                        d[(mn+i)] -= 1
                else:
                    return False
        
        return True