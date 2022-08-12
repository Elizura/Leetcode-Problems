# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum_ = 0):
            if not root:
                return False
            sum_ += root.val
            if not root.left and not root.right:
                return sum_ == targetSum
            
            return (dfs(root.left, sum_) or dfs(root.right, sum_))
        return dfs(root, sum_ = 0)