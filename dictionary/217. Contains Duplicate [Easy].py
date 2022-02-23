class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       # 1st version: faster than 30%
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                return True
        return False
      
      # need optimization - no need to use dictionary
      # 2nd version: faster than 91.29%
      hashmap = set()
        for i in nums:
            if i not in hashmap:
                hashmap.add(i)
            else:
                return True
        return False
