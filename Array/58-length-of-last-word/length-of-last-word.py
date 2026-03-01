class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                res += 1
            elif s[i] == ' ' and res > 0:
                return res
            else:
                continue

        return res