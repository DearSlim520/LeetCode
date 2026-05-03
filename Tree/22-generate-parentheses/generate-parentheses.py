class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(track: str, preCnt: int, postCnt: int):
            if len(track) == n * 2 and preCnt == postCnt:
                res.append(track[:])
                return
            if postCnt > preCnt:
                return
            
            for cur in ['(', ')']:
                if cur == '(' and preCnt < n:
                    backtrack(track + cur, preCnt + 1, postCnt)
                elif cur == ')' and preCnt > 0:
                    backtrack(track + cur, preCnt, postCnt + 1)
            return

        res = []
        backtrack('', 0, 0)
        return res