class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        trust_set = list(set(sum(trust, [])))
        N = len(trust_set)
        dic = {i:[0, 0] for i in trust_set} #[indegree, outdegree]
        for i in trust:
            dic[i[0]][1] += 1
            dic[i[1]][0] += 1
        for key in dic:
            if dic[key][1] == 0:
                if dic[key][0] == N - 1:
                    return key
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not trust and n == 1:
# 			return 1
# 		degree = [0 for i in range(0,n+1)]
# 		for u, v in trust:

# 			degree[u] -= 1 #indegree = -1 for that node
# 			degree[v] += 1 #outdegree = +1 for that node

# 		for i in degree:
# 			if i == (n - 1):
# 				return degree.index(i)
# 		return -1
        
        # if n == 1: return 1
        # adj = {}
        # for person in trust:
        #     if person[0] in adj:
        #         adj[person[0]].add(person[-1])
        #     else:
        #         adj[person[0]] = set([person[-1]])
        #     # adj[person[0]] = adj.get(person[0], set()).add(person[-1])
        # print(adj)
        # return 