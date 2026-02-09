class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution 1: clssic dp with space saving
        # globalMax = nums[0]
        # curMax = nums[0]
        # for i in range(1, len(nums)):
        #     curMax = max(nums[i], curMax + nums[i])
        #     globalMax = max(globalMax, curMax)
        
        # return globalMax

        # Solution 2: classic dp
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        maxVal = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            maxVal = max(maxVal, dp[i])

        return maxVal

