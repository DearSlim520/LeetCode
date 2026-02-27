class Solution:
    def jump(self, nums: List[int]) -> int:
        # choices: use / not use
        # dp[i] : step to the last (if can)
        # curr_furthest = i + nums[i]
        # dp[i] = 

        n = len(nums)
        if n == 1:
            return 0
        dp = [n] * n
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue
            else:
                curr_furthest = i + nums[i]
                if curr_furthest >= n-1:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i+1:curr_furthest+1]) + 1

        return dp[0]
            