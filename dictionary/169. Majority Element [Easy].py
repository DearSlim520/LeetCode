from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countdict = Counter(nums)
        
        return max(countdict, key = countdict.get)
