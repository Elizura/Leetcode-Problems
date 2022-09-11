# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([root])
        ans = 0
        while q:
            ans += 1
            a = q.popleft()
            if a.left: q.append(a.left)
            if a.right: q.append(a.right)
        return ans