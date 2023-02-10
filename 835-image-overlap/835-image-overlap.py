class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)
                
        
        idx1 = [(i//n,i%n) for i in range(n**2) if img1[i//n][i%n]]
        idx2 = [(j//n,j%n) for j in range(n**2) if img2[j//n][j%n]]
                                
        tr_vecs = Counter((i1-j1, i2-j2) for i1,i2 in idx1 for j1,j2 in idx2)                        
        
        return max(tr_vecs.values()) if tr_vecs else 0        