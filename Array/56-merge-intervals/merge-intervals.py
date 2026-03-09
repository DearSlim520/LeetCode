class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        start = 0
        maxEnd = intervals[0][1]
        for i in range(n):
            maxEnd = max(maxEnd, intervals[i][1])
            # non-overlap
            if i == n-1 or maxEnd < intervals[i+1][0]:
                if start == i:
                    res.append(intervals[i])
                else:
                    res.append([intervals[start][0], max(maxEnd, intervals[i][1])])
                start = i + 1
                

        return res
