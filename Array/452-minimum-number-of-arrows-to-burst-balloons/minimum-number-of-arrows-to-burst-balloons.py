class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        curMax = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > curMax:
                arrow += 1
                curMax = points[i][1]
            else:
                curMax = min(points[i][1], curMax)

        return arrow
            
