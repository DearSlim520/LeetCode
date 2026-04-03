class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = {}
        res = 0

        for num in nums:
            cur = sum(int(d) for d in str(num))
            if cur in seen:
                res = max(res, num + seen[cur])
                if num > seen[cur]:
                    seen[cur] = num
            else:
                seen[cur] = num

        return res if res > 0 else -1