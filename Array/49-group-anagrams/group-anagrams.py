class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        res = []
        seen = {}
        
        for s in strs:
            cur = ''.join(sorted(s))
            if cur in seen:
                res[seen[cur]].append(s)
            else:
                seen[cur] = len(res)
                res.append([s])

        return res