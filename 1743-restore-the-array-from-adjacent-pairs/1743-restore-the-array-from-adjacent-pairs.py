class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        allnums = set()
        for i, j in adjacentPairs:
            allnums.add(i)
            allnums.add(j)        
        init = -1                                            
        for ne1, ne2 in adjacentPairs:
            graph[ne1].append(ne2)
            graph[ne2].append(ne1)
        for n in graph:
            if len(graph[n]) == 1:
                init = n
                break
            
        ans = [init]
        positioned = set()
        positioned.add(init)
        def dfs(n):
            for neib in graph[n]:
                if neib not in positioned:
                    ans.append(neib)
                    positioned.add(neib)
                    dfs(neib)
        dfs(init)
        return ans