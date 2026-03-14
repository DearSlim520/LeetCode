class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        curNum = 0
        subtotal = 0
        sign = 1
        i, n = 0, len(s)

        while i < n:
            if s[i] == ' ':
                i += 1

            elif s[i].isdigit():
                while i < n and s[i].isdigit():
                    curNum = curNum * 10 + int(s[i])
                    i += 1
                subtotal += sign * curNum
                curNum = 0

            else:
                if s[i] in ('+','-'):
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    stk.append(subtotal)
                    stk.append(sign)
                    subtotal = 0
                    sign = 1
                else:
                    subtotal = stk.pop() * subtotal + stk.pop()
                i += 1
            

        return subtotal

