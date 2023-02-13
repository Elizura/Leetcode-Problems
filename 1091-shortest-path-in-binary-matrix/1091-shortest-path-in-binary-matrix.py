class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dist = [[1e9]*N for _ in range(M)]
        dist[0][0] = 0

        if grid[0][0]==1:
            return -1

        q = deque()
        q.append((0,0))

        dL = [-1, 0, 1]
        dR = [-1, 0, 1]

        while len(q)!=0:
            item = q.popleft()
            i = item[0]
            j = item[1]

            for x in dL:
                for y in dR:
                    ni = i+x
                    nj = j+y
                    if ni in range(N) and nj in range(M) and grid[ni][nj]==0:
                        if dist[i][j]+1<dist[ni][nj]:
                            dist[ni][nj] = dist[i][j]+1
                            q.append((ni, nj))

        # print(dist)
        return (dist[M-1][N-1]+1) if dist[M-1][N-1]!=1e9 else -1
            

