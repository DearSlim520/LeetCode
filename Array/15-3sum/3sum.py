class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        n = len(nums)
        while i < n - 2:
            cur = nums[i]
            temp_res = self.twoSum(nums, i+1, -1 * cur)
            for t in temp_res:
                t.append(cur)
                res.append(t)
            while i < n-1 and nums[i] == cur:
                i += 1

        return res

    def twoSum(self, nums: list[int], start: int, target: int) -> list[list[int]]:
        l, r = start, len(nums) - 1
        temp_res = []
        while l < r:
            left, right = nums[l], nums[r]
            if left + right < target:
                while l < r and nums[l] == left:
                    l += 1
            elif left + right > target:
                while l < r and nums[r] == right:
                    r -= 1
            else:
                temp_res.append([nums[l], nums[r]])
                while l < r and nums[l] == left:
                    l += 1
                while l < r and nums[r] == right:
                    r -= 1
                
        return temp_res
        

        