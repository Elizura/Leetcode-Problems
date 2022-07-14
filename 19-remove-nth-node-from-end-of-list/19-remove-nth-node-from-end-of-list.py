# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_ = head
        size = 0
        while cur_:
            cur_ = cur_.next
            size += 1
        
        
        dummy = ListNode (None, head)
        cur = dummy
        destination = size - n -1
        i =0 
        
        while i <= destination:
            cur = cur.next
            i += 1
            
        cur.next = cur.next.next
        
        return dummy.next
        
        
        