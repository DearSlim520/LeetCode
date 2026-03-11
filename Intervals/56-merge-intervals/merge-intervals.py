class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[start][1]:
                intervals[start][1] = max(intervals[start][1], intervals[i][1])
            else:
                res.append(intervals[start])
                start = i
        
        res.append(intervals[start])
        return res
