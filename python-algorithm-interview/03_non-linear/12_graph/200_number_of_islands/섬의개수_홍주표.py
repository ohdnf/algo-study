class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def find_island(row, col):
            grid[row][col] = "0"

            for drow, dcol in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < m and 0 <= ncol < n:
                    if grid[nrow][ncol] == "1":
                        find_island(nrow, ncol)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    find_island(r, c)
                    islands += 1

        return islands
