class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)             
        w = len([i for i in blocks[:k - 1] if i == 'W'])        
        ans = inf
        for right in range(k - 1, N):
            if blocks[right] == 'W':
                w += 1
            ans = min(ans, w)            
            if blocks[right - k + 1] == 'W':
                w -= 1            
        return ans
