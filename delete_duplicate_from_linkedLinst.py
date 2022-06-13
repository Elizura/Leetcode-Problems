class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        itr=head
        while itr:
            itr=itr.next
            count+=1
        itr=head
        for i in range(count-1):
            if i==count-2 and itr.val==itr.next.val:
                itr.next=None
                
            elif itr.val==itr.next.val:
                itr.next=itr.next.next
            else:
                itr=itr.next
        return head
