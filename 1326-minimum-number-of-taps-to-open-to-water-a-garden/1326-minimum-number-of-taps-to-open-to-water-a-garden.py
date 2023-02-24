class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)    		
        start = end = step = 0
        
        while end < n:
            step += 1
            start, end = end, max(i + max_range[i] for i in range(start, end + 1))
            if start == end:
                return -1
            
        return step