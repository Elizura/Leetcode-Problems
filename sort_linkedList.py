# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_list=[]
        cur=head
        while cur:
            new_list.append(cur.val)
            cur= cur.next
        new_list.sort()
        head=ListNode(new_list[0])
        temp=head
        i=1
        while i<len(new_list):
            temp.next=ListNode(new_list[i])
            temp=temp.next
            i+=1
            
        return head
        
