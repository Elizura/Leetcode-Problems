# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
                return False
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.left))
            stack.append((node1.left, node2.right))
        return True
        # l, r = [], []
#         if not root: return True        
#         left = deque()
#         right = deque()
#         left.append(root.left)
#         right.append(root.right)
#         while left and right:            
#             a = left.popleft()
#             b = right.popleft()
#             if a and b:
#                 if a.val != b.val:
#                     return False
#                 left.append(a.left)
#                 left.append(a.right)
#                 right.append(b.right)
#                 right.append(b.left)
#             elif not a and not b:
#                 pass
#             else:
#                 return False
#         return not left and not right
        
        
        
        
# #         def check(rootleft, rootright):
# #             if not rootleft and not rootright:
# #                 return True
# #             if not rootleft or not rootright:
# #                 return False
# #             return (rootleft.val == rootright.val) and (check(rootleft.left, rootright.right)) and (check(rootleft.right, rootright.left))
        
# #         if not root: return True
# #         return check(root.left, root.right)




#         def pst(root, visited, right):
#             print(visited, right)
#             if root is None:
#                 visited.append(None)
#                 return
#             if right:
#                 pst(root.right, visited, right)
#                 pst(root.left, visited, right)
#             else:
#                 pst(root.left, visited, right)
#                 pst(root.right, visited, right)

#             visited.append(root.val)

#         pst(root.left, l, False)
#         pst(root.right, r, True)
        

#         return l == r