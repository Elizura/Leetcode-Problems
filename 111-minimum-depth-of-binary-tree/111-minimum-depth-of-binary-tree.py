# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node, level):
            if not node: return
            l = dfs(node.left, level + 1)
            r = dfs(node.right, level + 1)
            if not l and not r: return level + 1
            if l and r: return min(l, r)
            return l if l else r
        return dfs(root, 0)
            