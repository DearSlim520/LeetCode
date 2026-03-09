class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # calculate neighbours
        for i in range(m):
            for j in range(n):
                ln = self.liveNeighbours(board, i, j, m, n)
                if board[i][j] == 0:
                    if ln == 3:
                        board[i][j] = 2 # to live
                elif board[i][j] == 1:
                    if ln < 2 or ln > 3:
                        board[i][j] = -1 # to die      

        # update simultaneously
        for i in range(m):
            for j in range(n):
                if board[i][j] <= 0:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
        
        return board
                    
        

    def liveNeighbours(self, board: List[List[int]], i: int, j: int, m: int, n: int) -> int:
        direction = [[-1, -1], [-1, 0], [-1,1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        cnt = 0
        for d in direction:
            if 0 <= i+d[0] < m and 0 <= j+d[1] < n:
                if abs(board[i+d[0]][j+d[1]]) == 1:
                    cnt += 1

        return cnt