class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def connect(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = 'T'
            connect(i, j-1)
            connect(i, j+1)
            connect(i-1, j)
            connect(i+1, j)

        # connect all O regions
        for i in range(m):
            connect(i, 0)
            connect(i, n-1)

        for j in range(n):
            connect(0, j)
            connect(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'