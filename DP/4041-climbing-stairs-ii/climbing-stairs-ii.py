class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n == 1:
            return costs[0] + 1
        if n == 2:
            return min(4, costs[0] + 2) + costs[1]
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = costs[0] + 1   # 2
        dp[2] = min(4, dp[1] + 1) + costs[1]   #min(4, 3) + 2 = 5

        for i in range(3, n+1):
            dp[i] = costs[i - 1] + min([9 + dp[i-3], 4 + dp[i-2], 1 + dp[i-1]])

        return dp[n]
            