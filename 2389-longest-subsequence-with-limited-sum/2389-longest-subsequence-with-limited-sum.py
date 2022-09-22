class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N = len(queries)
        answer = [0]*N
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
            
        def helper(idx): #binary search helper function
            return bisect_right(pref, queries[idx])
            # N = len(pref)
            # l, r = 0, N - 1
            # while r >= l:
            #     m = (l + r)//2
            #     if pref[m] > queries[idx]:
            #         r = m - 1
            #     else: # if it is less than or equal to
            #         l = m + 1
            # return l
            
        for j in range(N):
            answer[j] = helper(j)
        return answer
        