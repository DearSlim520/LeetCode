class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        single_sum = sum(arr)
        single_k = self.kadane(arr)
        if k == 1:
            return single_k % mod

        n = len(arr)
        cur = 0
        preMax, postMax = 0, 0

        # max prefix
        for x in arr:
            cur += x
            preMax = max(cur, preMax)

        cur = 0
        for x in arr[::-1]:
            cur += x
            postMax = max(cur, postMax)

        globalMax = max(
            single_k,
            preMax + postMax,
            preMax + postMax + (k - 2) * single_sum if single_sum > 0 else 0
        )

        return max(globalMax, 0) % mod

    def kadane(self, nums):
        cMax = gMax = float('-inf')
        for num in nums:
            cMax = max(num, cMax + num)
            gMax = max(gMax, cMax)
        return max(gMax, 0)