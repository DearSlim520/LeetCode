class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): 
            return False

        sp = tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        
        return True if sp == len(s) else False