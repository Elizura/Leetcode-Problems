class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        if not intervals or len(intervals)==1:
            return intervals
        for i in intervals:
            if not ans or ans[-1][-1]<i[0]:
                ans.append(i)
            else:
                ans[-1][-1]= max(ans[-1][-1],i[-1])
                
        return ans
