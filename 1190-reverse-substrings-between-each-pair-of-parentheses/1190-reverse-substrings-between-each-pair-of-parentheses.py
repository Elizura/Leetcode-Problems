class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                temp=''
                while stack[-1].isalpha():
                    temp+=stack[-1]
                    stack.pop()
                stack.pop()
                for i in temp:
                    stack.append(i)
                temp=''
                    
        return ''.join(stack)