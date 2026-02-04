class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1) [option]: choose this coin / not choose this coin
        #    [status]: the upper limit of capacity
        # 2）Simplify question:
        #    pack with capacity of [amount], N items, each weights coins[i - 1]
        # 3) State Transition Equation：
        #  dp[i][j] = the total amount is when ith coin, target amount is j

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # choose the ith coin
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][amount]

