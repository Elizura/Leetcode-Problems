class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            height_difference = heights[i+1] - heights[i]
            if height_difference <= 0:
                continue
            heapq.heappush(heap, height_difference)
            if len(heap) > ladders: 
                b = heapq.heappop(heap)
                bricks -= b
            if bricks < 0:
                return i 
                
        return len(heights)-1
            