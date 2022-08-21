# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            N = len(q)
            sum_ = 0            
            for i in range(len(q)):
                a = q.popleft()
                sum_ += a.val
                if a.left: q.append(a.left)                    
                if a.right: q.append(a.right)
            ans.append(sum_/ N) 
        return ans
                
        