# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            if root and not root.left and not root.right:
                return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.ans += abs(left - right)
            return left + right + root.val
            
        dfs(root)
        return self.ans