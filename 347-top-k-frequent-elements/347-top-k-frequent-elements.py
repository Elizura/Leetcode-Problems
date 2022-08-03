class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_ = collections.Counter(nums)
        # count_ = dict(count_)
        count = [(v,k) for k,v in count_.items()]
        heapq.heapify(count)
        while len(count) > k:
            heapq.heappop(count)
            
        return [i[1] for i in count]
            
        