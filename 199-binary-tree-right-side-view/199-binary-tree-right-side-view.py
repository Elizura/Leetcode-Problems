# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            N = len(q)
            for i in range(len(q)):
                a = q.popleft()
                if i == N - 1:
                    ans.append(a.val)
                if a.left: q.append(a.left)
                if a.right: q.append(a.right)
        return ans