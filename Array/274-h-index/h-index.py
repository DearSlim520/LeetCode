class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        i = 0
        res = 0
        while i < len(citations) and i + 1 <= citations[i]:
            res += 1
            i += 1
        
        return res