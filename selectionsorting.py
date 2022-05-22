class Solution: 
    def select(self, arr, i):
        _min = float('inf')
        for j in range(i, len(arr)):
            _min = min(_min, arr[j])
            
        return _min

    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            m=i
            for j in range(i,len(arr)):
                if arr[j]<arr[m]:
                    m=j
            arr[i],arr[m]=arr[m],arr[i]
        
        return arr
