class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        n=len(arr)
        ans=[]
        for i in range (n-1,-1,-1):
            max_=i
            for j in range(i,-1,-1):
                if arr[j]>arr[max_]:
                    max_=j
            if max_ !=i:
                flip(max_)
                flip(i)
                ans.append(max_+1)
                ans.append(i+1)
        return ans
        
