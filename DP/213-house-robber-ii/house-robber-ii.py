class Solution:
    def rob(self, nums: List[int]) -> int:
        # Simplify the question: Cannot rob both head and tail
        # Linear question head + linear question tail
        n = len(nums)
        curMax = 0
        # edge cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        dp1[1] = nums[0]
        dp2[2] = nums[0]

        for i in range(2, n+1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i - 1])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i - 1])

        return max(dp1[n-1], dp2[n])