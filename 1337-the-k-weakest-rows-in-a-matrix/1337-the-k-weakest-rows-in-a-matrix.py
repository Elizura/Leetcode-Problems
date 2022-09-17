class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = [collections.Counter(mat[i]) for i in range(len(mat))]
        temp = [(count[i][1], i) for i in range(len(count))]
        temp.sort()        
        return [temp[i][-1] for i in range(k)]