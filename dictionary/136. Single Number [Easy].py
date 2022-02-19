class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countdict = Counter(nums)
        for i in nums:
            if countdict[i] == 1:
                return i 
