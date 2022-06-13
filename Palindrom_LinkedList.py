# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l,r=head,head
        while r and r.next:
            l=l.next
            r=r.next.next
            
        prev=None
        curr=l
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        l,r=head,prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
            
