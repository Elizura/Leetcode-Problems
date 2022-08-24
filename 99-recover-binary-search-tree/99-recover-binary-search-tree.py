# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []
        # prev, next_ = None, None
        def dfs(node):
            if not node: return 
            dfs(node.left)
            res.append(node)
            dfs(node.right)
        dfs(root)
        a = sorted(i.val for i in res)
        for i in range(len(res)):
            res[i].val = a[i]
            # if self.res[i].val > self.res[i + 1].val:
            #     if not prev:prev = self.res[i + 1].val
            #     elif not next_: next_ = self.res.val
        # temp = prev
        # prev = next_
        # next_ = temp
        
        
        """
        Do not return anything, modify root in-place instead.
        """
        