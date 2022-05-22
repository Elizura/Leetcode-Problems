def countingSort(arr):
    result=[0]*100
    for i in arr:
        if i<100:
            result[i]+=1
            
    return result
