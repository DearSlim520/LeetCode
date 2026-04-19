class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        maxDiff = 0
        for j in range(len(nums2)):
            if nums2[j] >= nums1[i]:
                maxDiff = max(maxDiff, j - i)
            else: 
                if i < len(nums1) - 1: i += 1
            
        return maxDiff