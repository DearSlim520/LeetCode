class Solution:
    def jump(self, nums: List[int]) -> int:
        # initialization
        count = 0
        left, right = 0, len(nums) - 1
        
        # searching from the back
        while right > 0 and left < len(nums):
            if left + nums[left] >= right:
                count += 1
                right, left = left, 0
                continue
            left += 1
        return count
