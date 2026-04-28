class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def findborder(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            findborder(grid, i - 1, j)
            findborder(grid, i + 1, j)
            findborder(grid, i, j - 1)
            findborder(grid, i, j + 1)
            return

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    findborder(grid, i, j)
                    res += 1

        return res
        