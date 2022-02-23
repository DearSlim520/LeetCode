class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 1 - sort first
        nums = sorted(nums) 
        print(nums)
        
        # 2 - build hashtable
        hashmap = {}
        tmp = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                output = max(tmp, output)  # 4 - substitute max value
            else:
                hashmap[nums[i]] += 1
            
            # 3 - calculate sum value
            if nums[i]-1 in hashmap:
                tmp = hashmap[nums[i]-1] +  hashmap[nums[i]]
        output = max(tmp, output)  # 5 - consider the last round exception
        
        return output
         
