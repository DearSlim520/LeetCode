class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        curArrow = points[0][1]
        for p in points[1:]:
            if p[0] > curArrow:
                arrow += 1
                curArrow = p[1]
            else:
                curArrow = min(p[1], curArrow)

        return arrow
            
