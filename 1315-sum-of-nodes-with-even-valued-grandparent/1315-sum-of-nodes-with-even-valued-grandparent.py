# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sumv = 0
		# Mark the parent with even parent
        q = collections.deque([(root, 0)])
        while q:
            node, evenG = q.popleft()
            if node:
                if node.left:
				    # If parent was marked as evenG, add both the children value to res
                    if evenG:
                        sumv += node.left.val
                    q.append((node.left, not node.val % 2))
                if node.right:
                    if evenG:
                        sumv += node.right.val
                    q.append((node.right, not node.val % 2))
        return sumv
        # ans = 0
        # def dfs(node):
        #     nonlocal ans
        #     if not node: return 0
        #     if node.val % 2 == 0:
        #         if node.left:
        #             if node.left.left: ans += node.left.left.val
        #             if node.left.right: ans += node.left.right.val
        #         if node.right:
        #             if node.right.left: ans += node.right.left.val
        #             if node.right.right: ans += node.right.right.val
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return ans