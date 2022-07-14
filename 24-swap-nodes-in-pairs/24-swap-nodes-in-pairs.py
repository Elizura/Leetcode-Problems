# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        prev = ListNode(None, head)
        ans = head.next
        cur = head                
        while cur and cur.next:
            temp = cur.next        
            cur.next = cur.next.next
            temp.next = cur
            prev.next = temp
            cur = cur.next
            prev = prev.next.next
            
        return ans