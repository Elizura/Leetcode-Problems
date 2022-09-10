class Solution:
    def numTrees(self, n: int) -> int:
        memo = [1 for i in range(n + 1)]
        for node in range(2, len(memo)):
            total = 0
            for root in range(1, node + 1):
                left = root - 1                
                right = node - root
                total += memo[left] * memo[right]
            memo[node] = total
        return memo[-1]
                
            
        # return (math.factorial(2*n)) // (math.factorial(n + 1) * math.factorial(n))
        