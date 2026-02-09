class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        powerDict = {}
        for p in power:
            powerDict[p] = powerDict.get(p, 0) + 1
        
        unique = sorted(powerDict.keys())
        n = len(unique)

        dp = [0] * (n + 1) 
        dp[1] = unique[0] * powerDict[unique[0]]
        if n == 1: return dp[1]

        for i in range(2, n+1):
            curr = unique[i-1]
            curr_score = curr * powerDict[curr]

            # choose
            j = i - 1
            while j >= 1 and unique[j-1] >= curr - 2: # search for the last element available
                j -= 1
            prevSum = dp[j] if j >= 1 else 0
            dp[i] = max(dp[i-1], curr_score + prevSum)
            
        return dp[n]

