class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(cx, cy):
            grid[cx][cy] = "0"
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == "1":
                        dfs(nx, ny)

        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        return result