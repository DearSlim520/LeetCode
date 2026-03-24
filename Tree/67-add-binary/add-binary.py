class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            ai = int(a[i]) if i >= 0 else 0
            bj = int(b[j]) if j >= 0 else 0
            current = carry + ai + bj
            carry = current // 2
            res += str(current % 2)
            i -= 1
            j -= 1

        return res[::-1]