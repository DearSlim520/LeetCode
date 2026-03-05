class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        minLen = float('inf')
        curSum = 0
        while r <= n-1:
            curSum += nums[r]
            r += 1
            while l < r and curSum >= target:
                minLen = min(minLen, r - l)
                curSum -= nums[l]
                l += 1
            
            
        return minLen if minLen < float('inf') else 0
