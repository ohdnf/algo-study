class Solution(object):
    def numIslands(self, grid):
        di = [0, -1, 1, 0]
        dj = [-1, 0, 0, 1]
        def dfs(i, j):
            if grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < len(grid) and 0 <= nj <= nj < len(grid[0]):
                        dfs(ni, nj)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j) 
                    count += 1
        return count
            