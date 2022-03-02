class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict.fromkeys(s, 0)
        dict2 = dict.fromkeys(t, 0)
        
        for sub in s:
            dict1[sub] += 1
        
        for subt in t:
            dict2[subt] += 1
        
        if dict1 == dict2:
            return True
        return False
