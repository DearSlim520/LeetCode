class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0

        area = 0
        curArea, curSide = 0, 0
        # left to right
        for i in range(n):
            if height[i] > curSide:
                area += curArea
                curSide = height[i]
                curArea = 0
            else:
                curArea += curSide - height[i]

        curArea, curSide = 0, 0
        # right to left
        for i in range(n-1, -1, -1):
            if height[i] >= curSide:
                area += curArea
                curSide = height[i]
                curArea = 0
            else:
                curArea += curSide - height[i]
            
        return area