# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p: return True
        if p and not q: return False
        if q and not p: return False
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            for i in range(min(len(q1), len(q2))):
                a = q1.popleft()
                b = q2.popleft()
                if a.val != b.val: return False
                if a.left and b.left:
                           q1.append(a.left)
                           q2.append(b.left)
                if a.right and b.right:
                            q1.append(a.right)
                            q2.append(b.right)
                if not a.left:
                           if b.left: return False
                if not a.right:
                           if b.right: return False
                if not b.right:
                           if a.right: return False
                if not b.left:
                           if a.left: return False                 
        return False if q1 or q2 else True