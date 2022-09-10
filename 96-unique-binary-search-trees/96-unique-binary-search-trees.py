class Solution:
    def numTrees(self, n: int) -> int:
        return (math.factorial(2*n)) // (math.factorial(n + 1) * math.factorial(n))
        