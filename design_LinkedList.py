class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    

    def __init__(self):
        self.head=None
        self.length=0
        
    
    def ListLength(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    
    def get(self, index: int) -> int:
        if index>=self.ListLength() or  index<0 :
            return -1
        cur=self.head
        for i in range(index):
            cur=cur.next
        return cur.val
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        node=ListNode(val)
        node.next=self.head
        self.head=node        
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        node=ListNode(val)
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node
                
    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.ListLength() or index<0:
            return -1
        elif not self.head:
            self.head = ListNode(val)
            return
        
        elif index == 0:
            self.addAtHead(val)
            return
            
        elif index==self.ListLength():
            self.addAtTail(val)
            return
        
        elif index<self.ListLength():
            node=ListNode(val)
            cur=self.head 
            for i in range(index-1):
                cur=cur.next
            d = cur.next
            cur.next=node
            node.next=d
            return

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.ListLength() or index<0:
            return
        if index == 0:
            self.head = self.head.next
            return
            
        cur=self.head
        for i in range(index-1):
            cur=cur.next
        cur.next=cur.next.next
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
