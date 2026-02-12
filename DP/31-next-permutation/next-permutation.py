class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. find the spot the swap
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        # 2. if find the pivot, find the next available to swap digit from tail to head
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]

        # 3. swap
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
