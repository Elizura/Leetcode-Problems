# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, temp):
            # print([i.val for i in temp], [[b.val for b in a] for a in path])
            if not node:
                return
            if node.val == target.val:
                path.append(temp + [node])                
                return
            
            temp.append(node)
            dfs(node.left, temp)
            dfs(node.right, temp)
            # print([r.val for r in temp])
            temp.pop()
            
            
        path = []
        target = p
        dfs(root, [])
        
        target = q
        dfs(root, [])
                
        path_for_p = path[0]
        path_for_q = path[1]
        
        for i in range(min(len(path_for_p), len(path_for_q))):
            if path_for_p[i] != path_for_q[i]:
                return path_for_q[i-1]
        
        if len(path_for_p) < len(path_for_q):
            return path_for_p[-1]
        return path_for_q[-1]
        
#         # path_for_p path_for_q = [], []
#         path = []
        
#         def dfs(node,temp,path):
#             if not node:
#                 return
#             if node.val == p.val:
#                 path = temp + [node.val]
#                 return
#             temp.append(node.val)
#             dfs(node.right,temp, path)
#             dfs(node.left,temp, path)
#             temp.pop()
#             print(path,121212)
        
#         temp = []
#         target=p
#         dfs(root,temp, path)
#         print(path,11111)
#         path_for_p = path
        
#         temp = []
#         target=q
#         dfs(root,temp,path)
#         path_for_q = path
        
#         print(path_for_p)
#         print(path_for_q)
        
#         return
        
        
        
        
        
        
        
        
#         def dfs(node):            
#             if not node: return False
#             a.append(node.val)
#             if node.val == p.val:
#                 return True                         
#             if dfs(node.left) or dfs(node.right):                
#                 return True                        
#             a.pop()
#             return False
        
#         def dfs1(node):            
#             if not node: return False
#             b.append(node.val)
#             if node.val == q.val:
#                 return True                         
#             if dfs1(node.left) or dfs1(node.right):                
#                 return True
#             b.pop()            
#             return False
        
        
#         print(a, b)
#         if not root: return []
#         dfs(root)
#         dfs1(root)
#         i = 0
#         while i < len(a):
#             if a[i] != b[i]:
#                 return TreeNode(a[i - 1])
#             i += 1
                            
            