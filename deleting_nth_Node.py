def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        node = ListNode()
        node.next=head
        temp=node
        temp2=temp
        
        for i in range(n):
            temp2 = temp2.next
            
        while temp2.next:
            temp2 = temp2.next
            temp = temp.next
            
        temp.next = temp.next.next
        
        return node.next
