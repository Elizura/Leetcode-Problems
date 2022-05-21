def countSwaps(a):
    count=0
    for i in range(len(a)-1,-1,-1):
        for j in range(i):
            if a[j+1]<a[j]:
                count+=1
               
                a[j],a[j+1]=a[j+1],a[j]
               
    print('Array is sorted in',count,'swaps.')
    print('First Element:',a[0])
    print('Last Element:',a[len(a)-1])
