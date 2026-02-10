class Solution:
    def __init__(self):
        self.seen = {'(':0, ')':0}
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, "")
        return self.ans

    def backtrack(self, n: int, track: str):
        # if self.seen['('] == n and self.seen[')'] == n:
        if len(track) == n * 2:
            self.ans.append(track)
            return
        
        # pruning
        if self.seen['('] < n:
            self.seen['('] += 1
            self.backtrack(n, track + '(')
            self.seen['('] -= 1

        if self.seen[')'] < self.seen['(']:
            self.seen[')'] += 1
            self.backtrack(n, track + ')')
            self.seen[')'] -= 1

        return
