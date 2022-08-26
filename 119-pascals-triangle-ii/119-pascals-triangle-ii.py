class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        res = []
        for j in range(rowIndex + 1):
            res.append(self.factorial(rowIndex) // self.factorial(j)//self.factorial(rowIndex - j))
        return res
    
    def factorial(self, k):
        if k == 0:
            return 1
        else:
            return k * self.factorial(k - 1)