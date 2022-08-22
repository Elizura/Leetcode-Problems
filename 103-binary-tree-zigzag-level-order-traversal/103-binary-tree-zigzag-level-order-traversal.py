# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        level = 0
        while q:            
            temp = []            
            if level % 2 ==0:
                for i in range(len(q)):                     
                    a = q.popleft()                    
                    temp.insert(0, a.val)
                    if a.right: q.append(a.right)
                    if a.left: q.append(a.left)                                    
            else:
                for i in range(len(q)):
                    a = q.popleft()                    
                    temp.append(a.val)
                    if a.right: q.append(a.right)
                    if a.left: q.append(a.left)
            level += 1
            ans.append(temp)
        return ans