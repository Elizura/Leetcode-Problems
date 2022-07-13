#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        max_ = i
        left_child = 2*i+1
        right_child = 2*i+2
        
        if left_child < n and arr[left_child] > arr[max_]:
            max_ = left_child
        if right_child < n and arr[right_child] > arr[max_]:
            max_ = right_child
        if max_ != i:
            arr[max_], arr[i] = arr[i], arr[max_]
            self.heapify(arr,n,max_)
                
                
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        pass
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        for i in range((n//2)-1,-1,-1):
            Solution.heapify(self,arr,n,i)
        for i in range(len(arr)-1,0,-1):
            arr[0], arr[i] = arr[i], arr[0]
            Solution.heapify(self,arr,i,0)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends