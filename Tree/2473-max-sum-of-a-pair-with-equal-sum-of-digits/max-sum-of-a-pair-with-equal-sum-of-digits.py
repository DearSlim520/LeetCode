class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = {}
        res = 0
        nums.sort(reverse = True)
        print(nums)
        for num in nums:
            cur = sum(int(d) for d in str(num))
            if cur in seen:
                res = max(res, num + max(seen[cur]))
                # if num not in seen[cur]:
                #     seen[cur].append(num)
            else:
                seen[cur] = [num]

        return res if res > 0 else -1