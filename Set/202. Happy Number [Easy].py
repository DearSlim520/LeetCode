class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while True:
            if n == 1: return True
            elif n in visited: return False
            visited.add(n)
            n = sum(int(digit)**2 for digit in str(n))
