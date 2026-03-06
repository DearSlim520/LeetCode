class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for ss in s:
            seen[ss] = seen.get(ss, 0) + 1
        
        for tt in t:
            seen[tt] = seen.get(tt, 0) - 1
            if seen[tt] < 0:
                return False

        return True