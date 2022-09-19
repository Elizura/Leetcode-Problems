class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # N = len(set(sum(edges, [])))
        # edge_count = {}
        # for i in edges:            
        #     edge_count[i[0]] = edge_count.get(i[0], 0) + 1
        #     edge_count[i[1]] = edge_count.get(i[1], 0) + 1                  
        # for node, cnt in edge_count.items():
        #     if cnt == N - 1:
        #         return node
            
        cand1, cand2 = edges[0][0], edges[0][1]
        for i in edges[1:]:
            if cand1 not in i:
                return cand2
            if cand2 not in i:
                return cand1