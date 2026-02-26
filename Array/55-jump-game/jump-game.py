class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # options: use / not use this step
        # status: furthest index you can reach to, when take this step
        # state transition equition: dp[i] = max(furthest, num + i)

        furthest = 0
        n = len(nums)

        if n == 1:
            return True

        for i in range(n-1):
            if furthest < i:
                break
            furthest = max(furthest, i + nums[i])
            if furthest >= n - 1:
                return True

        return False
