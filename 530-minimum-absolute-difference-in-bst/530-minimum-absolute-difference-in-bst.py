# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans, prev = inf,  None
        def dfs(node):
            nonlocal ans, prev
            if not node: return
            dfs(node.left)
            if prev:
                ans = min(ans, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return ans
#         ans = inf
#         a = []
#         def dfs(node):
#             if not node: return
#             dfs(node.left)
#             a.append(node.val)
#             dfs(node.right)
#         dfs(root)
#         for i in range(len(a) - 1):
#             b = a[i] - a[i + 1]
#             if -b < ans: ans = -b
#         return ans
            
            
        