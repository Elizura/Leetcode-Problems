# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = []
        a = deque()
        a.append(root)
        while a:
            temp = []
            for i in range(len(a)):
                b = a.popleft()
                if b.left: a.append(b.left)
                if b.right: a.append(b.right)
                temp.append(b.val)
            ans.append(max(temp))
            temp = []
        return ans
            