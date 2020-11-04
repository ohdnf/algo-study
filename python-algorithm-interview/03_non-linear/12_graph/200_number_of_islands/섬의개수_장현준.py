class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def searchIslands(r, c, island_naming, grid, N, M):
            # 시작점 r,c & 네이밍 now
            grid[r][c] = island_naming
            s = [(r,c)]
            while s:
                r, c = s.pop()
                for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<M and grid[nr][nc] == "1":
                        grid[nr][nc] = island_naming
                        s.append((nr,nc))
                
        N = len(grid)
        M = len(grid[0])
        # 1. N x N 모든 좌표에서 섬을 탐색하기 시작한다. ( === "1" )
        # 2. 섬의 이름은 2부터 1씩 증가하며 네이밍 한다. 
        island_naming = 2
        for r in range(N):
            for c in range(M):
                if grid[r][c] == "1":
                    searchIslands(r, c, island_naming, grid, N, M)
                    island_naming += 1
        return island_naming-2

# 128 ms	15 MB	python3