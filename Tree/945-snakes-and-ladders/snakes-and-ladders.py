class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # given a num, return its position (i, j)
        def getPos(num) -> tuple:
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        # bfs
        q = deque([(1, 0)])
        visited = set([1])

        while q:
            pos, step = q.popleft()
            if pos == n * n:
                return step
            
            for nextPos in range(pos+1, min(pos+7, n*n + 1)):
                i, j = getPos(nextPos)
                curPos = board[i][j] if board[i][j] != -1 else nextPos  # take ladder if has
                if curPos not in visited:
                    visited.add(curPos)
                    q.append([curPos, step + 1])

        return -1