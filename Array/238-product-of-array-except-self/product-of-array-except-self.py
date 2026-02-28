class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left_prod = 1
        for i in range(n):
            res[i] = left_prod
            left_prod *= nums[i]

        right_prod = 1
        for j in range(n-1, -1, -1):
            res[j] *= right_prod
            right_prod *= nums[j]

        return res