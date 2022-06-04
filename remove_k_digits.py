def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        
        
        for i in range(len(num)):
            while stack and num[i]<stack[-1] and k:
                stack.pop()
                k-=1
            stack.append(num[i])
        
        
        stack=stack[:len(stack)-k]
        ans=''.join(stack)
        return str(int(ans)) if ans else "0"
