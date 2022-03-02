class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create new dictionaries from nums
        dict1 = dict.fromkeys(nums1, 0)
        dict2 = dict.fromkeys(nums2, 0)
        
        # construct dict1 with counting
        for i in nums1:
            dict1[i] += 1
        
        # record the overlap as a dictionary format
        for j in nums2:
            if dict1.get(j) and dict1[j]>0:
                dict2[j] += 1
                dict1[j] -= 1
            
        print(dict2.items())
        
        # convert to lists
        output = []
        for num, count in dict2.items():
            for _ in range(count):
                output.append(num)
                
        return output
