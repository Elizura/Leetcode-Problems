"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            ans = 0
            if not root: return 0
            if root.children:
                ans = max(dfs(i) for i in root.children)
            return ans + 1
        return dfs(root)
                