class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        mini = nums[0]

        for num in nums:
            res = max(res, num - mini)
            mini = min(mini, num)
            
        return res if res > 0 else -1