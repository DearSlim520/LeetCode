# Solution 1: O(n3)
def bruteForce(self, nums):
        out = []
        nums.sort()
        added = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and (a, b, c) not in added:
                        out.append([a, b, c])
                        added.add((a, b, c))
        return out
        
# Solution 2: Start - End pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        added = set()
        output = []
        for i in range(len(nums)):
            cur = nums[i]
            start, end = 0, i - 1
            while start < end:
                if nums[start] + nums[end] == -cur:
                    if (cur, nums[start], nums[end]) not in added:
                        output.append([cur, nums[start], nums[end]])
                    added.add((cur, nums[start], nums[end]))
                    
                    start += 1
                elif nums[start] + nums[end] < -cur:
                    start += 1
                else:
                    end -= 1
        return output
