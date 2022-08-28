# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node1, node2):            
            if node1.val == target.val: return node2 
            l = dfs(node1.left, node2.left) if node1.left else None                                        
            r = dfs(node1.right, node2.right) if node1.right else None        
            return l if l else r                        
        return dfs(original, cloned)
        