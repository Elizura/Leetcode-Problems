class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        pref = shifts.copy()        
        alphabets = string.ascii_lowercase                
        dic = {alphabets[i]: i for i in range(len(alphabets))}
        for i in range(len(shifts) - 2, -1, -1):
            pref[i] += pref[i + 1]
            
        ans = ''
        for i in range(len(s)):
            idx = (dic[s[i]] + pref[i]) % 26
            ans += alphabets[idx]
        return ans