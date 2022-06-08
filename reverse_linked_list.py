class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l,r=None,head
        while r:
            temp=r.next
            r.next=l
            l=r
            r=temp
        return l
