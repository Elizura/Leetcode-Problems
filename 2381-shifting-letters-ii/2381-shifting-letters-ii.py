class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        shift = [0] * (N + 1)
        
        for start, end, direction in shifts:
            if direction == 0:
                shift[start] -= 1
                shift[end + 1] += 1
            else: #direction == 1
                shift[start] += 1
                shift[end + 1] -= 1
                
        pref = shift.copy()
        for i in range(1, len(pref)):
            pref[i] += pref[i - 1]
        
        alphabets = string.ascii_lowercase
        alpha_dict = {alphabets[i]: i for i in range(len(alphabets))}
        ans = ''
        for j in range(N):            
            idx = (alpha_dict[s[j]] + pref[j]) % 26
            ans += alphabets[idx]
            
        return ans
            
                            
        '''
        [[0, 1, 0], [0, 1, 1]]
        sweep-ing
        forward shifts = 1 and backward shift = -1
        a b c
        0 1 2
        1  -1 
        "dztz"
        0, 1, 2, 3, 4
        [0, 0, 0, 0, 0]
        shift = [-1, 2, -1, 0, 0]        
        pref = [-1, 1, 0, 0, 0]
        catz
        -1 % 26 = 25
        '''