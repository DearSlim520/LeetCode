class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        for key in self.dict:
            if key in vec.dict:
                output += self.dict[key] * vec.dict[key]
        return output
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
