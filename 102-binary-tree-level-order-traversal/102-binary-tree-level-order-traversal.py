# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, temp = [], []
        if not root: return []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                a = q.popleft()
                temp.append(a.val)
                if a.left: q.append(a.left)
                if a.right: q.append(a.right)
                
            ans.append(temp)
            temp = []
        return ans
                
        