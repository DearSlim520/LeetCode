class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # necessarity of sort
        # sort: [0, 1, 3, 5, 6]
        # [6, 5, 3, 1, 0]

        # n - i >= nums[i]

        citations.sort(reverse = True)
        i = 0
        res = 0
        while i < len(citations) and i + 1 <= citations[i]:
            res += 1
            i += 1
        
        return res