from collections import deque
class Solution:
    def maximumSwap(self, num: int) -> int:

        str_num = str(num)

        numb_indices = {}

        for idx, char in enumerate(str_num):
            if char not in numb_indices:
                numb_indices[char] = deque([idx])
            
            else:
                 numb_indices[char].append(idx)


        for idx, char in enumerate(str_num):
            max_ele = max(numb_indices.keys())
            if char < max_ele:
                rightest_idx = numb_indices[max_ele][-1]
                return int(str_num[:idx]+max_ele+str_num[idx+1:rightest_idx]+str_num[idx]+str_num[rightest_idx+1:])
            else:
                numb_indices[char].popleft()
                if len(numb_indices[char]) == 0:
                    del numb_indices[char]

        return num