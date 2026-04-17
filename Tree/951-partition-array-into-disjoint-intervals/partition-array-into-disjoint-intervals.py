class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lMax = visitedMax = nums[0]
        n = len(nums)
        res = 1
        for i in range(1, n):
            if lMax > nums[i]:
                res = i + 1
                lMax = visitedMax
            else:
                visitedMax = max(visitedMax, nums[i])
                
        return res
