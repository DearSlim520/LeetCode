class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        minSum = float('inf')
        self.memo = [[666666 for _ in range(n)] for _ in range(n)]

        # start from different column
        for j in range(n):
            minSum = min(minSum, self.dp(matrix, n-1, j))

        return minSum

    # dfs?
    def dp(self, matrix: List[List[int]], i: int, j: int) -> int:
        # end condition
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return float('inf')
        # base case
        if i == 0:
            return matrix[0][j]
        # search in memo, to avoid dup calculation
        if self.memo[i][j] != 666666:
            return self.memo[i][j]

        self.memo[i][j] = matrix[i][j] + min(
            self.dp(matrix, i-1, j - 1),
            min(self.dp(matrix, i-1, j),
                self.dp(matrix, i-1, j + 1))
        )
        return self.memo[i][j]

    