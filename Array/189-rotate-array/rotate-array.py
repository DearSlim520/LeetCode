class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 经典：三步反转法
        if k == 0:
            return nums

        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

        return nums
        
    def reverse(self, nums: List[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1