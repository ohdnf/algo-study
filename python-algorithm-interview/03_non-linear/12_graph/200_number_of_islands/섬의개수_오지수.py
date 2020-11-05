class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        result = 0

        def find_island(x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and grid[nx][ny] == '1':
                    visit[nx][ny] = 1
                    find_island(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visit[i][j]:
                    visit[i][j] = 1
                    find_island(i, j)
                    result += 1

        return result
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        result = 0

        def find_island(x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and grid[nx][ny] == '1':
                    visit[nx][ny] = 1
                    find_island(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visit[i][j]:
                    visit[i][j] = 1
                    find_island(i, j)
                    result += 1

        return result


solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

