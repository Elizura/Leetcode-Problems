# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def dfs(node, low, high):
            if not node: return 0
            if low <= node.val <= high: ans[0] += node.val
            dfs(node.left, low, high)
            dfs(node.right, low, high)
            return ans[0]
        return dfs(root, low, high)
        # ans = 0
        # a = deque()
        # a.append(root)
        # while a:
        #     f = a.popleft()
        #     if low <= f.val and f.val <= high: ans += f.val
        #     if f.left: a.append(f.left)
        #     if f.right: a.append(f.right)            
        # return ans
        