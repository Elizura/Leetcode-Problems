# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        node1, node2 = None, None
        q = deque()
        q.append([root, None, 0])        
        while q:
            for i in range(len(q)):
                a = q.popleft()                
                if a[0].val == x: node1 = a
                if a[0].val == y: node2 = a
                if a[0].left: q.append([a[0].left, a[0], a[2] + 1])
                if a[0].right: q.append([a[0].right, a[0], a[2] + 1])
        if node1[1] and node2[1]:
            if node1[1].val != node2[1].val and node1[2] == node2[2]:
                return True
        else: return False
            
                