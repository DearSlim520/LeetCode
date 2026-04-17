class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word_cnt = {}
        n = len(words)
        for word in words:
            for char in word:
                word_cnt[char] = word_cnt.get(char, 0) + 1
        
        for val in word_cnt.values():
            if val % n != 0:
                return False

        return True