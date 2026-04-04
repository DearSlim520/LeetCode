class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        numStr = str(num)
        for nu in numStr:
            if int(nu) % 2 == 1:
                odd.append(int(nu))
            else:
                even.append(int(nu))

        odd.sort()
        even.sort()
        
        res = 0
        for nu in numStr:
            if int(nu) % 2 == 1:
                res = res * 10 + odd.pop()
            else:
                res = res * 10 + even.pop()

        return res