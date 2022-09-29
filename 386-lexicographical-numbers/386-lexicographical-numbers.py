class Solution:
    def lexicalOrder(self, n: int) -> List[int]:        
        arr = list(map(int, sorted(list(map(str, [i for i in range(1, n + 1)])))))        
        return arr