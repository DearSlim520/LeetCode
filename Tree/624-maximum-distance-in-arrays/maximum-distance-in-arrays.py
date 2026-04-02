class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = arrays[0][0], arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, abs(maxi - arrays[i][0]), abs(arrays[i][-1] - mini))
            mini = min(mini, arrays[i][0])
            maxi = max(maxi, arrays[i][-1])

        return res