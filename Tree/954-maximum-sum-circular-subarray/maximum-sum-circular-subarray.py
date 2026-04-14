class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cMax = cMin = gMax = gMin = nums[0]
        for num in nums[1:]:
            cMax = max(num, cMax + num)
            gMax = max(gMax, cMax)

            cMin = min(num, cMin + num)
            gMin = min(gMin, cMin)

        maxCircle = sum(nums) - gMin
        if gMax < 0:
            return gMax
        return max(maxCircle, gMax)