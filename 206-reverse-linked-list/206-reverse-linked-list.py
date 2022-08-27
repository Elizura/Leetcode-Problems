# Definition for singly-linked list.
# class ListNode(object):
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        back=None
        main=head
        front=head.next
        while front:
            main.next = back
            back = main
            main = front
            front = front.next

        main.next = back
        return main