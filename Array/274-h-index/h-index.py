class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        res = 0
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return res
            res += 1
        
        return res