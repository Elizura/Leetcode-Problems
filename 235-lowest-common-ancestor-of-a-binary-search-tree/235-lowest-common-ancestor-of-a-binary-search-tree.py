# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, a, b):
            if (a.val > node.val and b.val < node.val) or (a.val < node.val and b.val > node.val): return node
            if a.val > node.val and b.val > node.val:
                return dfs(node.right, a, b)
            if a.val < node.val and b.val < node.val:
                return dfs(node.left, a, b)
            return a if node.val == a.val else b
        return dfs(root, p, q)
            
                
            
#         def dfs(node):
#             if not node: return
#             if node == p or node == q:
#                 return node
#             l = dfs(node.left)
#             r = dfs(node.right)
#             if not l and not r: return 
#             if l and r: return node
#             return l if l else r
#         return dfs(root)
        
            
        