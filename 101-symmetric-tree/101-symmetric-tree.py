# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True        
        left = deque()
        right = deque()
        left.append(root.left)
        right.append(root.right)
        while left and right:            
            a = left.popleft()
            b = right.popleft()
            if a and b:
                if a.val != b.val:
                    return False
                left.append(a.left)
                left.append(a.right)
                right.append(b.right)
                right.append(b.left)
            elif not a and not b:
                pass
            else:
                return False
        return not left and not right
        
        
        
        
#         def check(rootleft, rootright):
#             if not rootleft and not rootright:
#                 return True
#             if not rootleft or not rootright:
#                 return False
#             return (rootleft.val == rootright.val) and (check(rootleft.left, rootright.right)) and (check(rootleft.right, rootright.left))
        
#         if not root: return True
#         return check(root.left, root.right)