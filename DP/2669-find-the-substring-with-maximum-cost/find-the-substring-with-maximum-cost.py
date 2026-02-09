class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # create a full list with all values
        nums = []
        for letter in s:
            if letter not in chars:
                nums.append(ord(letter) - ord('a') + 1)
            else:
                index = chars.index(letter)
                nums.append(vals[index])

        # dp
        n = len(nums)
        if n == 1: return max(nums[0], 0)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        globalMax = dp[1]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1] + nums[i-1], nums[i-1])
            globalMax = max(globalMax, dp[i])

        return max(globalMax, 0)
            