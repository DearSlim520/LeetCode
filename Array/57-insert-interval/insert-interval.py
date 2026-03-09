class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for r in intervals:
            if r[1] < newInterval[0]:
                res.append(r)
            elif r[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = r
            else:
                newInterval[0] = min(r[0], newInterval[0])
                newInterval[1] = max(r[1], newInterval[1])
        res.append(newInterval)
                
        return res