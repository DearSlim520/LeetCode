class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # hash map to store the pad
        max_cnt = [3] * 10
        max_cnt[7], max_cnt[9] = 4, 4

        mod = 10 ** 9 + 7
        
        # Calculate the total amount of each letter, order by sequence
        groups = []
        starter = 0
        while starter < len(pressedKeys):
            j = starter
            while j < len(pressedKeys) and pressedKeys[j] == pressedKeys[starter]:
                j += 1
            groups.append((pressedKeys[starter], j - starter))
            starter = j

        ans = 1
        
        for key, value in groups:
            curMaxCnt = max_cnt[int(key)]
            dp = [0] * (value + 1)
            dp[0] = 1
            
            # when i count of letter, when j count of letter duplicates
            for i in range(1, value + 1):
                for j in range(1, min(curMaxCnt, i) + 1):
                    dp[i] = (dp[i] + dp[i - j]) % mod
            
            ans = (ans * dp[value]) % mod

        return ans
                    