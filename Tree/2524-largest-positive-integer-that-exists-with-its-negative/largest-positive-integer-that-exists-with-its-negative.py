class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in seen:
            if num>0 and -num in seen:
                res = max(res, num)

        return res if res > 0 else -1