# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            nonlocal ans
            if not node: return 0            
            left = dfs(node.left)
            right = dfs(node.right)
            temp_sum = max(node.val, node.val + left, node.val + right, node.val + left + right)
            ans = max(ans, temp_sum)
            return max(left + node.val, right + node.val, node.val)
        dfs(root)
        return ans