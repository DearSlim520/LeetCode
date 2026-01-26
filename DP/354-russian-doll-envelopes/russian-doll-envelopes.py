class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1])) # sort by width, if same, sort by height desc
        height = [envelopes[i][1] for i in range(n)]
        
        return self.dp(height)

    # bisection
    def dp(self, nums: List[int]) -> int:
        piles = 0
        n = len(nums)
        top = [0] * n
        for i in range(n):
            curPoker = nums[i]

            # sliding window
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] >= curPoker:
                    right = mid
                else:
                    left = mid + 1
            # if need to add a new pile
            if left == piles: 
                piles += 1
            top[left] = curPoker
                
        return piles