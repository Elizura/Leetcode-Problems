class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        matrix = sum(matrix, [])
        heapq.heapify(matrix)
        i = 0
        while i < k:
            a = heapq.heappop(matrix)
            ans.append(a)
            i += 1
            
        return ans[-1]
            