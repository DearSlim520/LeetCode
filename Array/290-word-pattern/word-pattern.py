class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        
        seen = {}
        used = set()
        for p, ss in zip(pattern, s.split()):
            if ss in seen:
                if seen[ss] != p:
                    return False
            else:
                if p in used:
                    return False
                seen[ss] = p
                used.add(p)

        return True