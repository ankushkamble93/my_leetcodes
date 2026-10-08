class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if grid[i][j] == "0" or grid[i][j] == "-1":
                return
            grid[i][j] = "-1"
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i+1, j)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands+=1
                    dfs(i, j)
        return islands