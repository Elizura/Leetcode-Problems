    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        return Solution.fib(self,n-1)+Solution.fib(self,n-2)
