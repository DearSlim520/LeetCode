class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        curArrow = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > curArrow:
                arrow += 1
                curArrow = points[i][1]
            else:
                curArrow = min(points[i][1], curArrow)

        return arrow
            
