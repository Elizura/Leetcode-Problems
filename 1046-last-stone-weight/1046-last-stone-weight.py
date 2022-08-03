class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            a = heapq.nsmallest(1, stones)
            heapq.heappop(stones)
            b = heapq.nsmallest(1, stones)
            heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, (a[0] - b[0]))

        return 0 if len(stones) == 0 else abs(stones[0])