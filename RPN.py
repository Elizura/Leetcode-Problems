class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                if i=='+':
                    a=stack[-1]+stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i=='-':
                    a=stack[-2]-stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i=='*':
                    a=stack[-1]*stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i=='/':
                    a=stack[-2]/stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))

        return int(stack[-1])
        
