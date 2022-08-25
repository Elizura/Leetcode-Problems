# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return
            if node.val == p.val or node.val == q.val:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if not l and not r: return
            if l and r: return node
            return l if l else r
        return dfs(root)
            
#         def dfs(node, temp):            
#             if not node:
#                 return
#             if node.val == target.val:
#                 path.append(temp + [node])                
#                 return
            
#             temp.append(node)
#             dfs(node.left, temp)
#             dfs(node.right, temp)
#             # print([r.val for r in temp])
#             temp.pop()
            
            
#         path = []
#         target = p
#         dfs(root, [])
        
#         target = q
#         dfs(root, [])
                
#         path_for_p = path[0]
#         path_for_q = path[1]
        
#         for i in range(min(len(path_for_p), len(path_for_q))):
#             if path_for_p[i] != path_for_q[i]:
#                 return path_for_q[i-1]
        
#         if len(path_for_p) < len(path_for_q):
#             return path_for_p[-1]
#         return path_for_q[-1]
        
# #         a = []
# #         def dfs(node, target):            
# #             if not node: return False
# #             a.append([node.val])
# #             if node.val == target.val:
# #                 return True                         
# #             if dfs(node.left, target) or dfs(node.right, target):  
# #                 return True                        
# #             a.pop()
# #             return False    
                                
# #         if not root: return []
        
# #         dfs(root, q)
# #         dfs(root, p)        
# #         print(a)
# #         # print(path_p, path_q)
# #         # i = 0
# #         # while i < len(a):
# #         #     if a[i] != b[i]:
# #         #         return TreeNode(a[i - 1])
# #         #     i += 1
                            
            