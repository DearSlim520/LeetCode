class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(track: List[int], curSum: int, start: int):
            if target == curSum:
                ans.append(track[:])
                return
            if target < curSum:
                return
            for i in range(start, n):
                track.append(candidates[i])
                backtrack(track, curSum + candidates[i], i)
                track.pop()
            return

        ans = []
        n = len(candidates)
        backtrack([], 0, 0)
        return ans