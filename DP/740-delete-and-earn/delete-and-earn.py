class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        uni_nums = sorted(dict.keys())
        n = len(uni_nums)
        if n == 1:
            return dict[uni_nums[0]] * uni_nums[0]

# dp approach
        # dp = [0] * (n + 1)
        # dp[1] = dict[uni_nums[0]] * uni_nums[0]
        # for i in range(2, n + 1):
        #     curr = uni_nums[i-1]
        #     prev = uni_nums[i-2]
        #     curr_score = dict[curr] * curr
        #     if curr == prev + 1:
        #         dp[i] = max(curr_score + dp[i-2], dp[i-1])
        #     else:
        #         dp[i] = curr_score + dp[i-1]

        # return dp[n]

# robbery approach (improve the space complication)
        prev1 = dict[uni_nums[0]] * uni_nums[0]
        prev2 = 0
        for i in range(1, n):
            curr = uni_nums[i]
            curr_score = dict[curr] * curr
            if curr == uni_nums[i-1] + 1:
                curr = max(curr_score + prev2, prev1)
            else:
                curr = curr_score + prev1
            prev2 = prev1
            prev1 = curr

        return curr