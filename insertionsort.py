def insertionSort1(n, arr):
    # Write your code herefor i in range(1,n):
    for i in range(1,len(arr)):
        key = arr[i]
        while i>0 and arr[i-1] > key:
            arr[i] = arr[i-1]
            i-=1
            print(' '.join([str(i) for i in arr]))
        arr[i] = key
    print(' '.join([str(i) for i in arr]))
