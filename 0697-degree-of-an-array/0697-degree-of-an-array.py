class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        target = max([i for i in count.values()])
        left, N = 0, len(nums)
        dic = defaultdict(int)
        ans = N
        _max = [-1, -inf]
        for right in range(N):            
            c = nums[right]
            dic[c] += 1
            if dic[c] > _max[-1]:
                _max = [c, dic[c]]
            while _max[-1] == target:
                ans = min(ans, right - left + 1)
                k = nums[left]
                dic[k] -= 1
                if k == _max[0]:
                    _max[-1] -= 1 
                left += 1
        return ans