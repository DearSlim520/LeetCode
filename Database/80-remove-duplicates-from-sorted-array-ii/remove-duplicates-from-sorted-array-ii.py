class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                cnt = 1
            else:
                cnt += 1
                if cnt > 2:
                    continue
            
            nums[k] = nums[i]
            k += 1

        return k
                