class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add

        while n != 1:
            nextN = 0
            for s in str(n):
                nextN += int(s) **  2
            if nextN not in seen:
                seen.add(nextN)
            else:
                return False
            n = nextN
        
        return True