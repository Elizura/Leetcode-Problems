class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        count = [(-v, k) for k,v in count.items()]
        heapq.heapify(count)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(count)[1])
            
        return ans
        