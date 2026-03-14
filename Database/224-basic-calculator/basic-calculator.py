class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        sign = 1
        curSum, subtotal = 0, 0
        stk = []

        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                while i < n and s[i].isdigit():
                    curSum = curSum * 10 + int(s[i])
                    i += 1
                subtotal += sign * curSum
                curSum = 0
            else:
                if s[i] in ('+', '-'):
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    stk.append(subtotal)
                    stk.append(sign)
                    sign = 1
                    subtotal = 0
                else:
                    subtotal = stk.pop() * subtotal + stk.pop()
                i += 1
        
        return subtotal