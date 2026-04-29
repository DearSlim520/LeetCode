class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        # 1. find the element to start with
        start = len(nums) - 2
        while start >= 0:
            if nums[start] < nums[start + 1]:
                break
            start -= 1
        
        # 2. swap the start point with "next" bigger adjusent number
        right = len(nums) - 1
        if start >= 0:
            while right >= start and nums[right] <= nums[start]:
                right -= 1
            nums[start], nums[right] = nums[right], nums[start]

        # 3. sort the right part
        left, right = start + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
        