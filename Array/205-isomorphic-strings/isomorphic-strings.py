class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        used = set()

        for sc, tc in zip(s, t):
            if sc not in seen:
                if tc in used:
                    return False
                seen[sc] = tc
                used.add(tc)
            else:
                if seen[sc] != tc:
                    return False

        return True