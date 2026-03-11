class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for i in range(1, len(points)):
            if points[i-1][0] <= points[i][0] <= points[i-1][1]:
                points[i][1] = min(points[i-1][1], points[i][1])
            else:
                res += 1

        return res + 1
