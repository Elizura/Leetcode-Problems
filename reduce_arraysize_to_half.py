class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        r = 0
        c = collections.Counter(arr)
        li = [i for i in c.values()]
        li.sort(reverse=True)
        sum_sw = li[0]
        if len(li)==1:
            return 1
        for i in range(len(arr)):
            if sum_sw >= len(arr)//2:
                return r+1
            else:
                r+=1
                sum_sw+=li[r]
