# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return
            if node == p or node == q:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if not l and not r: return 
            if l and r: return node
            return l if l else r
        return dfs(root)
        
            
        