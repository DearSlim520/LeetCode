class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        start = 0
        for i in range(n):
            if i == 0 or nums[i-1] < nums[i] - 1:
                start = i
            # end

            if (i < n-1 and nums[i+1] > nums[i] + 1) or i == n-1:
                if start < i:
                    res.append(str(nums[start]) + '->' + str(nums[i]))
                elif start == i:
                    res.append(str(nums[i]))

        return res