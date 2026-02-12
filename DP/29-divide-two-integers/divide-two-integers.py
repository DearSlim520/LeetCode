class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # get sign
        sign = 1
        if (dividend < 0) != (divisor < 0):
            sign = -1

        # abs
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        
        # calculate the multiple value
        equotient = 0
        while divisor <= dividend:
            temp = divisor
            multiple = 1
            while (temp << 1) <= dividend:
                temp <<= 1
                multiple <<= 1
                
            dividend -= temp
            equotient += multiple
                
        result = sign * equotient

        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        return result
            