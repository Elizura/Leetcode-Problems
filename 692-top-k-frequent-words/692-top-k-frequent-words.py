class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        count = collections.Counter(words)
        
        count = [(-v,k) for k,v in count.items()]
        heapq.heapify(count)
        for i in range(k):
            a = heapq.heappop(count)
            ans.append(a[1])
        
        return ans
    
        