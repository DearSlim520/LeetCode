class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 4
        prev1 = 2
        prev2 = 1
        for i in range(2, n+1):
            curr = (prev1 + prev2) % mod
            prev2 = prev1
            prev1 = curr
        
        return (curr * curr) % mod
