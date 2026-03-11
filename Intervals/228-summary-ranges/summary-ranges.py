class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        res = []
        n = len(nums)
        start = 0
        for i in range(n):
            if i == n-1 or (nums[i+1] > nums[i] + 1):
                if start < i:
                    res.append(str(nums[start]) + '->' + str(nums[i]))
                elif start == i:
                    res.append(str(nums[i]))
                start = i + 1

        return res