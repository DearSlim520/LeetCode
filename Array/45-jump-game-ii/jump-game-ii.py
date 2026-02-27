class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        if n == 1:
            return 0

        for i in range(n-2, -1, -1):
            if nums[i] > 0:
                curr_furthest = i + nums[i]
                if curr_furthest >= n-1:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i+1:curr_furthest+1]) + 1

        return dp[0]
            