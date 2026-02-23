class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # approach 1
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     if nums[right] == val:
        #         right -= 1
        #     else:
        #         if nums[left] == val:
        #             nums[left] = nums[right]
        #             left += 1
        #             right -= 1
        #         else:
        #             left += 1

        # return left 

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k