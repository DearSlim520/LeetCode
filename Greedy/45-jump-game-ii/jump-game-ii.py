class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        step = 0
        curr_furthest = 0
        global_furthest = 0

        for i in range(n-1):
            global_furthest = max(global_furthest, i + nums[i])
            if i == curr_furthest:
                step += 1
                curr_furthest = global_furthest
            if curr_furthest >= n+1:
                break

        return step
