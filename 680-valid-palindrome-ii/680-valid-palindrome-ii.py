class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while r >= l:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1        
        while r >= l:            
            if s[l] != s[r]:
                a = isPalindrome(s[:l] + s[l + 1:])
                b = isPalindrome(s[:r] + s[r +1:])
                if not a and not b: return False
                else: return True                
            else:
                r -= 1
                l += 1
        return True
    # a=s[::-1]
    # i=0
    # j=len(s)-1
    # if(s==a):
    #     return True
    # else:
    #     while(i<j):
    #         if(s[i]==s[j]):
    #             i=i+1
    #             j=j-1
    #         elif(s[i+1:j+1]==s[i+1:j+1][::-1]):
    #             return True
    #         elif(s[i:j]==s[i:j][::-1]):
    #             return True
    #         else:
    #             return False
    #     return False