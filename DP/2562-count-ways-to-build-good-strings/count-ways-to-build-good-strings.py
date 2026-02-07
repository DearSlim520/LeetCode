class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # selection: add zero or one
        # status: current count 
        # dp[i] = when total i letters, there are VALUE of combinations
        # state transition eqaution: if zero / one: dp[i - zero] / dp[i - one]
        # for i in range(high + 1):
        #  for s in [zero_str, one_str]:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        res = 0

        # base case
        dp[0] = 1

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]

            if i >= low and i <= high:
                res += dp[i]

        return res if res < mod else res%mod