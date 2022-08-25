# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        def dfs(node, temp = ""):
            if not node: return
            if not node.right and not node.left:
                arr.append(temp + str(node.val))
                return
            
            dfs(node.left, temp + str(node.val) + "->")
            dfs(node.right, temp + str(node.val) + "->")
                   
        dfs(root)
        return arr
        