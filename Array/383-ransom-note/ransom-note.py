class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for m in magazine:
            dic[m] = dic.get(m, 0) + 1
        
        for r in ransomNote:
            dic[r] = dic.get(r, 0) - 1
            if dic[r] < 0:
                return False

        return True