class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 2-d choice: 1/2, status: current min(cost)
        # dp[i][w]
        # dp[i][w] = min(dp[i-1], dp[i-2]) + cost[i-1]

        n = len(cost)
        dp = [0] * (n+1)
        dp[1], dp[2] = cost[0], cost[1]

        for i in range(3, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]

        return min(dp[n-1], dp[n])