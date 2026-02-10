class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, "", 0, 0)
        return self.ans

    def backtrack(self, n: int, track: str, left: int, right: int):
        if len(track) == n * 2:
            self.ans.append(track)
            return
        
        # pruning
        if left < n:
            self.backtrack(n, track + '(', left + 1, right)

        if right < left:
            self.backtrack(n, track + ')', left, right + 1)

        return
