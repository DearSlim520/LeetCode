# 1 - O(n), create another list
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output = [0] * len(nums)
        for i in range(len(nums)):
            if i + k >= len(nums):
                output[k - len(nums) + i] = nums[i]
            else:
                output[k + i] = nums[i]
        print(output)

# 2 - O(n) solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        
        length = len(nums)
        for i in range(len(nums)-k):
            nums.append(nums[i])
        
        del nums[:-length]

 # 3 - 
