class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLength = 0
        for i, n in enumerate(nums):
            if i > maxLength: 
                return False
            maxLength = max(maxLength, i+n)
        return True
                
