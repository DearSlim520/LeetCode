class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(track, used):
            if len(nums) == len(track):
                ans.append(track[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    track.append(nums[i])
                    used[i] = True
                    backtrack(track, used)
                    track.pop()
                    used[i] = False

        ans = []
        used = [False] * len(nums)
        backtrack([], used)
        return ans

        