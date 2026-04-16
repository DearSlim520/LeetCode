class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry:
            if digits[i] < 9:
                digits[i] += carry
                carry = 0
            else:
                digits[i] = 0
                carry = 1
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits