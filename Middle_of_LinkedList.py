class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        itr=head
        while itr:
            itr=itr.next
            count+=1
        itr=head
        for i in range(count//2):
            itr=itr.next
        return itr
