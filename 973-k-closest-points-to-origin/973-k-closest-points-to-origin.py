class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        ans = []
        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(maxHeap, (-d, point))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        return [i[-1] for i in maxHeap]
                
 