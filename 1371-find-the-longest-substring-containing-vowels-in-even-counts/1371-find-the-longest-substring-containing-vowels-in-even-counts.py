class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s),-1,-1):
            for x in range(len(s) - i +1):
                counter = 0
                temp = s[x:x+i]
                for k in 'aeiou':
                    if temp.count(k) % 2 != 0:
                        counter += 1
                        break
                if counter == 0:
                    return i
    
