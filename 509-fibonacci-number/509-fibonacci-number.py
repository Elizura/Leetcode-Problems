class Solution:
    dic = {}
    def fib(self, n: int) -> int:
        if n in self.dic: return self.dic[n]
        if n == 0: return 0
        if n <= 2: return 1
        self.dic[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dic[n]
        