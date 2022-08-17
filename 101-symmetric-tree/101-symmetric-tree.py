# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(rootleft, rootright):
            if not rootleft and not rootright:
                return True
            if not rootleft or not rootright:
                return False
            return (rootleft.val == rootright.val) and (check(rootleft.left, rootright.right)) and (check(rootleft.right, rootright.left))
        
        if not root: return True
        return check(root.left, root.right)