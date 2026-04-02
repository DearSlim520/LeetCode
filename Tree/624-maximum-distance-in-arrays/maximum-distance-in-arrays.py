class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = arrays[0][0], arrays[0][-1]
        res = 0
        for arr in arrays[1:]:
            res = max(res, abs(maxi - arr[0]), abs(arr[-1] - mini))
            mini = min(mini, arr[0])
            maxi = max(maxi, arr[-1])

        return res