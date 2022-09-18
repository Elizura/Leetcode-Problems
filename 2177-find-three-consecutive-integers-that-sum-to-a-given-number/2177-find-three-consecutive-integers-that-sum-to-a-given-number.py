class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num - 3)/3
        if int(x) != x: return []
        
        return [int(x + i) for i in range(3)]