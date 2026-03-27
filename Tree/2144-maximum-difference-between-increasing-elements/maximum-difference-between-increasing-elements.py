class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        mini = nums[0]

        for num in nums:
            if num > mini:
                res = max(res, num - mini)
            else:
                mini = num
            
        return res