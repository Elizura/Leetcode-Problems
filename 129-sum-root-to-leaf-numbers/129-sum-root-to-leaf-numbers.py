# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = []
        def dfs(node, sum_ = 0):
            sum_ += node.val
            if not node.left and not node.right:
                ans.append(sum_)
                return 
            if node.left: dfs(node.left, sum_*10)
            if node.right: dfs(node.right, sum_*10)
        dfs(root, 0)
        return sum(ans)
        