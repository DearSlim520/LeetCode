class Solution:
    def __init__(self):
        self.seen = {'(':0, ')':0}
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, [])
        return self.ans

    def backtrack(self, n: int, track: List[str]):
        if len(track) == n * 2:
            curStr = ''.join(track)
            if curStr not in self.ans:
                self.ans.append(curStr)
            return
        
        for x in ['(',')']:
            # pruning:
            if self.seen[x] == n:
                continue
            if x == ')' and self.seen['('] == self.seen[')']:
                continue

            # make choice
            track.append(str(x))
            self.seen[x] += 1
            self.backtrack(n, track)
            # cancel choice
            track.pop()
            self.seen[x] -= 1

        return
