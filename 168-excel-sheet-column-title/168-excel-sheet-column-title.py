class Solution:
    dicty={i:chr(65+i) for i in range(26)}
    def convertToTitle(self, columnNumber: int) -> str:
        i=0
        while True:
            if columnNumber-26**i<0:
                i-=1
                break
            columnNumber-=26**i
            i+=1
        res=""
        for j in range(i,-1,-1):
            res=res+self.dicty[columnNumber//(26**j)]
            columnNumber-=26**j*(columnNumber//(26**j))
        return res