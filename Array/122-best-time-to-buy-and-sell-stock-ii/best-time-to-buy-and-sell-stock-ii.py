class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        dp0, dp1 = 0, -prices[0]

        for i in range(1, n):
            dp0 = max(dp0, dp1 + prices[i]) # nothing / sell today
            dp1 = max(dp1, dp0 - prices[i])     # hold / buy today

        return dp0