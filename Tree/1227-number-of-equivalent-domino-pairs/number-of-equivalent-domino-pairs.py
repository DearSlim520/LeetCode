class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        res = 0
        for do in dominoes:
            if do[0] > do[1]:
                key = (do[1], do[0])
            else:
                key = (do[0], do[1])
            
            if key in seen:
                res += seen[key]
            seen[key] = seen.get(key, 0) + 1

        return res