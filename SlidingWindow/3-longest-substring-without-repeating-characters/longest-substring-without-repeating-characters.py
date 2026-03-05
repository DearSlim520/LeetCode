class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        curWindow = {}
        n = len(s)
        
        while r < n:
            cur = s[r]
            r += 1
            curWindow[cur] = curWindow.get(cur, 0) + 1
            while l < r and curWindow[cur] > 1:
                curWindow[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l)

            

        return maxLen
            