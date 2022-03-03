class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict.fromkeys(s, 0)
        for letter in s:
            dic[letter] += 1

        ranked = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        print(ranked)
        
        output = str()
        for i, j in ranked:
            for _ in range(j):
                output += i
        
        return output
