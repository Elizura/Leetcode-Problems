class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabets = string.ascii_uppercase                
        dic = {alphabets[i]: 0 for i in range(26)}
        _max = 0
        left = 0
        N = len(s)
        ans = -inf
        for right in range(N):              
            dic[s[right]] += 1
            _max = max(_max, dic[s[right]])
            while (right - left + 1) - (_max) > k:
                dic[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)    
        return ans
            #extend window