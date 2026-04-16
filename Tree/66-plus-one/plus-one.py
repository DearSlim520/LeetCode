class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += carry
                carry = 0
                break
            else:
                if carry == 0:
                    break
                digits[i] = 0
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits