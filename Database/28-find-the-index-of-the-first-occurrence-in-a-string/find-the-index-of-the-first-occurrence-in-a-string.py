class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h):
            if i + n - 1 < h and haystack[i:i+n] == needle:
                return i

        return -1