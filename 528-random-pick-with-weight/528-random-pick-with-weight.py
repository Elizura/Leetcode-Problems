class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1,self.n):
            w[i] += w[i-1]
        self.s = self.w[-1]
    def pickIndex(self) -> int:
        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()