# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):            
            if not node: return
            if node.left: l = node.left
            if not node.left: l = None
            if node.right: r = node.right
            if not node.right: r = None        
            node.left = r
            node.right = l            
            dfs(l)
            dfs(r)            
        
        dfs(root)
        return root