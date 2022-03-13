class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlen = 0
        for x in nums:
            tmp = 1
            if x - 1 not in nums:
                while x+1 in nums:
                    tmp += 1
                    x += 1
                    
                maxlen = max(maxlen, tmp)
                
        return maxlen
