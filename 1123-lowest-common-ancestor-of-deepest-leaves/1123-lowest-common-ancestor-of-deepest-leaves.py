# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        maxd, dep, anssofar = 0, 0, []
        def dfs(node, dep):
            nonlocal maxd
            maxd = max(maxd, dep)
            if not node: return dep
            l = dfs(node.left, dep + 1)
            r = dfs(node.right, dep + 1)            
            if l == r == maxd:
                anssofar.append(node)
            return max(l, r)
        dfs(root, 0)
        return anssofar[-1]