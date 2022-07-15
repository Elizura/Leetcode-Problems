class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            
            if b > a:
                heapq.heappush(stones, a-b)
                
        if not stones:
            return 0
                
        return abs(stones[0])