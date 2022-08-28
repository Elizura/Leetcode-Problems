# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node1, node2):            
            if node1.val == target.val:
                return node2
            if node1.left:
                l = dfs(node1.left, node2.left)
            if not node1.left:
                l = None
            if node1.right:
                r = dfs(node1.right, node2.right)
            if not node1.right:
                r = None            
            return l if l else r
        
        
        a = dfs(original, cloned)
        return a
        