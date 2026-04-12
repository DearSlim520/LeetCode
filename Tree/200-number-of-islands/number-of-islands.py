class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.findBorder(grid, i, j)

        return res

    def findBorder(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        
        self.findBorder(grid, i, j-1)
        self.findBorder(grid, i, j+1)
        self.findBorder(grid, i-1, j)
        self.findBorder(grid, i+1, j)
            