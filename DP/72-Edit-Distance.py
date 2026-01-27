class Solution:
    def __init__(self):
        self.memo = []
    
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(word1, m-1, word2, n-1)

    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        # base case: when only one str is empty
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # if memo has value
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        # write into memo
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i - 1, s2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(s1, i, s2, j - 1) + 1,
                self.dp(s1, i - 1, s2, j) + 1,
                self.dp(s1, i - 1, s2, j - 1) + 1
            )

        return self.memo[i][j]
        
