# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not node1 and not node2: return True
            if node1 and not node2: return False
            if not node1 and node2: return False
            if node1.val != node2.val: return False
            l = same(node1.left, node2.left)
            r = same(node1.right, node2.right)
            if l and r: return True
        return same(p, q)