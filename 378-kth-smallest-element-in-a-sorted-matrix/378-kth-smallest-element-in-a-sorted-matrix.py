class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in matrix:
            for j in i:
                ans.append(j)
                
        ans.sort()
        return ans[k-1]