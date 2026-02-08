class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        mod = 10**9 + 7
        ans = 0

        dp = [0] * (maxLength + 1)
        dp[0] = 1

        for i in range(1, maxLength + 1):
            if i >= zeroGroup:
                dp[i] += dp[i - zeroGroup]
            if i >= oneGroup:
                dp[i] += dp[i - oneGroup]
            if i >= minLength and i <= maxLength:
                ans += dp[i]


        return ans if ans<mod else ans % mod