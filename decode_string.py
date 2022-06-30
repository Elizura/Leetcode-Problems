class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                s_inside=''
                the_no=''
                while stack[-1].isalpha():                    
                    s_inside=stack.pop()+s_inside
                while stack[-1]=='[':
                    stack.pop()
                while stack and stack[-1].isdigit():
                    the_no=stack.pop()+the_no
                stack.append(int(the_no)*s_inside)
                
        return ''.join(stack)
        
