class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []        
        
        
    def addNum(self, num: int) -> None:
        # print(self.maxHeap, self.minHeap)
        if not self.minHeap and not self.maxHeap:             
            heapq.heappush(self.minHeap, num)
        elif self.minHeap and not self.maxHeap:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
                a = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -a)                    
            else:
                heapq.heappush(self.maxHeap, -num)         
        elif len(self.minHeap) == len(self.maxHeap) + 1:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
                a = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -a)                
            else:
                heapq.heappush(self.maxHeap, -num)           
        elif len(self.minHeap) == len(self.maxHeap):            
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)   
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)                
            else:
                heapq.heappush(self.maxHeap, -num)
                a = heapq.heappop(self.maxHeap) 
                heapq.heappush(self.minHeap, -a)
                
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0]))/2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()