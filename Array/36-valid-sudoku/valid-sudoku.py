class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in rows[i] or cur in cols[j] or cur in boxes[(i//3)*3 + (j//3)]:
                    return False
                rows[i].add(cur)
                cols[j].add(cur)
                boxes[(i//3)*3 + (j//3)].add(cur)
            
        return True