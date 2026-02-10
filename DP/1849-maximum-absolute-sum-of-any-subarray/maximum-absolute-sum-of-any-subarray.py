class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curMin, curMax = 0, 0
        globalMax = 0
        for num in nums:
            curMin = min(num, curMin + num)
            curMax = max(num, curMax + num)
            globalMax = max(abs(globalMax), abs(curMax), abs(curMin))

        return globalMax