# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list=[]
        cur=head
        while cur:
            new_list.append(cur.val)
            cur= cur.next
        new_list.sort()
        head=ListNode(0)
        temp=head
        for i in new_list:
            temp.next=ListNode(i)
            temp=temp.next
            
        return head.next
        
