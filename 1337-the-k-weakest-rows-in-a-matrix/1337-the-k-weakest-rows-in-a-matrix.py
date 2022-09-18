class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = [(-collections.Counter(mat[i])[1], -i) for i in range(len(mat))]           
        heapq.heapify(count)        
        while len(count) > k:            
            heapq.heappop(count)
        count.sort(reverse = True)
        return [-count[i][-1] for i in range(len(count))]