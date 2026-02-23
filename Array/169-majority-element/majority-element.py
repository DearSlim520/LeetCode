class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. O(n log n)
        # nums.sort()
        # return nums[len(nums)//2]

        # 2. O(1)
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += (1 if candidate == num else -1)

        return candidate