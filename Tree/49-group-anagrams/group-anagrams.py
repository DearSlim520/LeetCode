class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        seen = {}
        res = []
        for str in strs:
            cur = ''.join(sorted(str))
            if cur in seen:
                res[seen[cur]].append(str)
            else:
                seen[cur] = len(res)
                res.append([str])
        
        return res