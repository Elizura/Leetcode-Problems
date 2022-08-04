# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        heap = []
        for i,v in enumerate(lists): 
            if v: heapq.heappush(heap, (v.val, i)) 
            
        dummy = cur = ListNode(0)
        
        while heap:
            first_ele, index = heapq.heappop(heap)
            cur.next = ListNode(first_ele)  
            second_ele = lists[index].next 
            if second_ele:
                heapq.heappush(heap, (lists[index].next.val, index))
                lists[index] = lists[index].next
            cur = cur.next
        return dummy.next
        
        
        